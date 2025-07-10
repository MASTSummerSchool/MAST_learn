import os
import platform
import cv2
import numpy as np
import urllib.request
import urllib.parse
import requests
import json
import base64
import datetime
from pathlib import Path

try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import img_to_array
    from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
    HAS_KERAS = True
except ImportError:
    try:
        from keras.models import load_model
        from keras.preprocessing.image import img_to_array
        from keras.applications.mobilenet_v3 import preprocess_input
        HAS_KERAS = True
    except ImportError:
        HAS_KERAS = False


def compose_path(filename: str, file_ext: str = '.jpg') -> str:
    """
    Compose the path to save captured images.

    Parameters:
    filename (str): The name of the file.
    file_ext (str): The file extension (default: '.jpg').

    Returns:
    str: The path to the file.
    """
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")

    # Create path based on OS
    if platform.system() == "Windows":
        sep = '\\'
        home_dir = os.getenv('HOMEDRIVE')
        home_path = os.getenv('HOMEPATH')
        if home_dir is not None and home_path is not None:
            config_dir = home_dir + home_path
        else:
            # Fallback to user profile or current directory
            config_dir = os.getenv('USERPROFILE', os.getcwd())
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home if home is not None else os.getcwd()

    # Create the data directory
    data_dir = config_dir + sep + 'webcam_images'

    # Check if it exists, create if not
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    file_dir = data_dir + sep + filename + file_ext
    return file_dir


def capture_webcam_image(camera_index: int = 0) -> str:
    """
    Capture an image from the webcam and save it temporarily.

    Parameters:
    camera_index (int): Index of the camera to use (default: 0 for primary camera).

    Returns:
    str: Path to the captured image file.
    """
    if not isinstance(camera_index, int) or camera_index < 0:
        raise ValueError("camera_index deve essere un intero non negativo.")

    # Initialize webcam
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise RuntimeError(
            f"Impossibile accedere alla webcam con indice {camera_index}")

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        cap.release()
        raise RuntimeError("Impossibile catturare l'immagine dalla webcam")

    # Release the camera
    cap.release()

    # Save the captured image with unique timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")[
        :-3]  # Include milliseconds
    temp_path = compose_path(f"webcam_capture_{timestamp}", ".jpg")
    cv2.imwrite(temp_path, frame)

    print(f"Immagine catturata e salvata in: {temp_path}")
    return temp_path


def load_custom_model(model_path: str = "mobilenet_NOME_v1.keras"):
    """
    Load a custom trained model from local file or URL with automatic .keras to .h5 conversion.

    Parameters:
    model_path (str or keras.Model): Local filename, URL to the model file, or already loaded model.

    Returns:
    model: The loaded Keras model.
    """
    if not HAS_KERAS:
        raise ImportError(
            "Keras non è installato. Installare con: pip install keras")

    # Se è già un modello caricato, restituiscilo subito
    if hasattr(model_path, "predict") and hasattr(model_path, "save"):
        print("✅ Modello già caricato, nessun caricamento necessario.")
        return model_path

    # Check if it's a URL
    if isinstance(model_path, str) and model_path.startswith(('http://', 'https://')):
        final_model_path = _download_model_from_url(model_path)
    else:
        # Local file - compose path
        final_model_path = _get_local_model_path(
            model_path) if isinstance(model_path, str) else model_path

    # Check if model exists
    if not os.path.exists(final_model_path):
        raise FileNotFoundError(f"Modello non trovato: {final_model_path}")

    # Automatic .keras to .h5 conversion for better compatibility
    if isinstance(final_model_path, str) and final_model_path.endswith('.keras'):
        h5_path = final_model_path.replace('.keras', '_auto_converted.h5')
        # Converti solo se il .h5 non esiste o è più vecchio del .keras
        if not os.path.exists(h5_path) or os.path.getmtime(h5_path) < os.path.getmtime(final_model_path):
            h5_path = _auto_convert_keras_to_h5(final_model_path)
        final_model_path = h5_path if h5_path else final_model_path
        print(
            f"🔄 Modello .keras convertito o già presente come .h5: {final_model_path}")

    # Load the model with enhanced error handling
    try:
        model = load_model(final_model_path, compile=False)
        print(f"✅ Modello caricato (compile=False): {final_model_path}")
        return model
    except Exception as e:
        print(f"⚠️ Errore caricamento con compile=False: {e}")
        try:
            model = load_model(final_model_path)
            print(f"✅ Modello caricato (standard): {final_model_path}")
            return model
        except Exception as e2:
            print(f"⚠️ Errore caricamento standard: {e2}")
            raise RuntimeError(
                f"Impossibile caricare il modello: {final_model_path}. Vedere dettagli sopra.")


def _get_tf_version() -> str:
    """Get TensorFlow version for debugging."""
    try:
        import tensorflow as tf
        return tf.__version__
    except:
        return "Non disponibile"


def _detect_model_format(model_path: str) -> str:
    """Detect model format for debugging."""
    if not os.path.exists(model_path):
        return "File non esistente"

    if os.path.isdir(model_path):
        return "SavedModel (directory)"

    if model_path.endswith('.keras'):
        return "Keras (.keras)"
    elif model_path.endswith('.h5'):
        return "HDF5 (.h5)"
    elif model_path.endswith('.pb'):
        return "Protocol Buffer (.pb)"
    else:
        return f"Formato sconosciuto ({os.path.splitext(model_path)[1]})"


def verify_model_compatibility(model_path: str) -> dict:
    """
    Verify model compatibility and provide diagnostic information.

    Parameters:
    model_path (str): Path to the model file.

    Returns:
    dict: Diagnostic information about the model.
    """
    import tensorflow as tf

    info = {
        "path": model_path,
        "exists": os.path.exists(model_path),
        "format": _detect_model_format(model_path),
        "tensorflow_version": _get_tf_version(),
        "size_mb": 0,
        "loadable": False,
        "error": None,
        "suggestions": []
    }

    if info["exists"]:
        try:
            if os.path.isfile(model_path):
                info["size_mb"] = round(
                    os.path.getsize(model_path) / (1024*1024), 2)

            # Try loading with different methods
            try:
                model = load_model(model_path, compile=False)
                info["loadable"] = True
                info["input_shape"] = str(model.input_shape) if hasattr(
                    model, 'input_shape') else "N/A"
                info["output_shape"] = str(model.output_shape) if hasattr(
                    model, 'output_shape') else "N/A"
                info["layers_count"] = len(
                    model.layers) if hasattr(model, 'layers') else 0
            except Exception as e:
                info["error"] = str(e)
                info["suggestions"].append("Provare con compile=False")

                if ".keras" in model_path:
                    info["suggestions"].append(
                        "Convertire a formato .h5 se possibile")
                    info["suggestions"].append(
                        "Verificare compatibilità versione TensorFlow")

        except Exception as e:
            info["error"] = str(e)
    else:
        info["suggestions"].append("Verificare che il file esista")
        info["suggestions"].append("Controllare il percorso del file")

    return info


def _auto_convert_keras_to_h5(keras_path: str) -> str:
    """
    Automatically convert .keras file to .h5 format with caching.

    Parameters:
    keras_path (str): Path to the .keras file.

    Returns:
    str: Path to the converted .h5 file, or None if conversion failed.
    """
    if not keras_path.endswith('.keras'):
        return None

    # Generate .h5 path
    h5_path = keras_path.replace('.keras', '_auto_converted.h5')

    # Check if already converted and cached
    if os.path.exists(h5_path):
        # Check if .h5 file is newer than .keras file
        keras_mtime = os.path.getmtime(keras_path)
        h5_mtime = os.path.getmtime(h5_path)
        if h5_mtime > keras_mtime:
            print(f"📁 Usando modello .h5 già convertito: {h5_path}")
            return h5_path
        else:
            print(f"🔄 Modello .keras più recente, riconversione necessaria")

    # Attempt automatic conversion
    try:
        print(f"🔄 Conversione automatica {keras_path} → {h5_path}")

        # Try to load the .keras model with different methods
        model = None
        load_methods = [
            lambda: load_model(keras_path, compile=False),
            lambda: load_model(keras_path),
        ]

        for i, method in enumerate(load_methods):
            try:
                model = method()
                print(
                    f"✅ Modello .keras caricato per conversione (metodo {i+1})")
                break
            except Exception as e:
                print(f"⚠️ Metodo {i+1} fallito: {e}")
                continue

        if model is None:
            print(f"❌ Impossibile caricare .keras per conversione")
            return None

        # Save as .h5
        model.save(h5_path, save_format='h5')
        print(f"✅ Conversione automatica completata: {h5_path}")

        # Verify the converted model
        try:
            test_model = load_model(h5_path, compile=False)
            print(f"✅ Verifica conversione automatica riuscita")
            return h5_path
        except Exception as e:
            print(f"⚠️ Problemi con il modello convertito: {e}")
            # Return the path anyway, it might still work
            return h5_path

    except Exception as e:
        print(f"⚠️ Conversione automatica fallita: {e}")
        return None


def convert_model_format(input_path: str, output_path: str = None, target_format: str = "h5") -> str:
    """
    Convert model between different formats to solve compatibility issues.

    Parameters:
    input_path (str): Path to input model.
    output_path (str): Path for output model (optional).
    target_format (str): Target format ('h5', 'keras', 'saved_model').

    Returns:
    str: Path to converted model.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Modello non trovato: {input_path}")

    # Generate output path if not provided
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        if target_format == "h5":
            output_path = f"{base_name}_converted.h5"
        elif target_format == "keras":
            output_path = f"{base_name}_converted.keras"
        elif target_format == "saved_model":
            output_path = f"{base_name}_converted_savedmodel"
        else:
            raise ValueError(f"Formato non supportato: {target_format}")

    try:
        print(f"🔄 Conversione modello da {input_path} a {output_path}")

        # Load the model with best method available
        model = None
        load_methods = [
            lambda: load_model(input_path, compile=False),
            lambda: load_model(input_path),
        ]

        for i, method in enumerate(load_methods):
            try:
                model = method()
                print(f"✅ Modello caricato con metodo {i+1}")
                break
            except Exception as e:
                print(f"⚠️ Metodo {i+1} fallito: {e}")
                continue

        if model is None:
            raise RuntimeError(
                "Impossibile caricare il modello con nessun metodo")

        # Save in target format
        if target_format == "h5":
            model.save(output_path, save_format='h5')
        elif target_format == "keras":
            model.save(output_path, save_format='keras')
        elif target_format == "saved_model":
            model.save(output_path, save_format='tf')
        else:
            raise ValueError(
                f"Formato di output non supportato: {target_format}")

        print(f"✅ Modello convertito salvato: {output_path}")

        # Verify the converted model loads correctly
        try:
            test_model = load_model(output_path, compile=False)
            print(f"✅ Verifica conversione riuscita")
            return output_path
        except Exception as e:
            print(f"⚠️ Problemi con il modello convertito: {e}")
            return output_path

    except Exception as e:
        error_msg = f"❌ Errore durante la conversione: {str(e)}"
        print(error_msg)
        raise RuntimeError(error_msg)


def _get_local_model_path(model_name: str) -> str:
    """Get the full path for a local model file."""
    if platform.system() == "Windows":
        sep = '\\'
        home_dir = os.getenv('HOMEDRIVE')
        home_path = os.getenv('HOMEPATH')
        if home_dir is not None and home_path is not None:
            config_dir = home_dir + home_path
        else:
            config_dir = os.getenv('USERPROFILE', os.getcwd())
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home if home is not None else os.getcwd()

    # Create the model directory path
    model_dir = config_dir + sep + 'models'

    # Create directory if it doesn't exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    return model_dir + sep + model_name


def _download_model_from_url(url: str) -> str:
    """Download a model from URL and cache it locally."""
    try:
        # Parse URL to get filename
        parsed_url = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename or not filename.endswith('.keras'):
            filename = "downloaded_model.keras"

        # Get cache directory
        cache_dir = _get_model_cache_dir()
        cached_model_path = os.path.join(cache_dir, filename)

        # Check if already cached
        if os.path.exists(cached_model_path):
            print(f"Modello trovato in cache: {cached_model_path}")
            return cached_model_path

        # Download the model
        print(f"Downloading model from: {url}")
        urllib.request.urlretrieve(url, cached_model_path)
        print(f"Modello scaricato e salvato in: {cached_model_path}")

        return cached_model_path

    except Exception as e:
        raise RuntimeError(
            f"Errore durante il download del modello da {url}: {str(e)}")


def _get_model_cache_dir() -> str:
    """Get the model cache directory."""
    if platform.system() == "Windows":
        sep = '\\'
        home_dir = os.getenv('HOMEDRIVE')
        home_path = os.getenv('HOMEPATH')
        if home_dir is not None and home_path is not None:
            config_dir = home_dir + home_path
        else:
            config_dir = os.getenv('USERPROFILE', os.getcwd())
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home if home is not None else os.getcwd()

    # Create cache directory
    cache_dir = config_dir + sep + 'models' + sep + 'cache'

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    return cache_dir


def predict_image_custom(model, image_path: str, class_names: list = None):
    """
    Make prediction on an image using a custom trained model.

    Parameters:
    model: The trained Keras model.
    image_path (str): Path to the image file.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    tuple: (predicted_class, confidence_score)
    """
    if not HAS_KERAS:
        raise ImportError(
            "Keras non è installato. Installare con: pip install keras")

    # Use provided class names or default ones
    if class_names is None or len(class_names) == 0:
        class_names = [
            "aqualy", "calcolatrice_casio", "bicchiere", "iphone13", "mouse_wireless",
            "pennarello_giotto", "persona", "webcam_box"
        ]

    CLASS_NAMES = class_names

    IMG_SIZE = (224, 224)

    # Check if image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Immagine non trovata: {image_path}")

    # Load and preprocess the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Impossibile caricare l'immagine: {image_path}")

    # Resize and preprocess
    image = cv2.resize(image, IMG_SIZE)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make prediction
    predictions = model.predict(img_array)

    # Get predicted class and confidence
    predicted_class_idx = np.argmax(predictions)
    predicted_class = CLASS_NAMES[predicted_class_idx]
    confidence_score = float(predictions[0][predicted_class_idx])

    print(f"Classe predetta: {predicted_class}")
    print(f"Confidence score: {confidence_score:.4f}")

    return predicted_class, confidence_score


def predict_image_label(model, image_path: str, class_names: list = None) -> str:
    """
    Get only the predicted label for an image using a custom trained model.

    Parameters:
    model: The trained Keras model.
    image_path (str): Path to the image file.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    str: The predicted label.
    """
    predicted_class, _ = predict_image_custom(model, image_path, class_names)
    return predicted_class


def predict_image_confidence(model, image_path: str, class_names: list = None) -> float:
    """
    Get only the confidence score for an image using a custom trained model.

    Parameters:
    model: The trained Keras model.
    image_path (str): Path to the image file.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    float: The confidence score.
    """
    _, confidence_score = predict_image_custom(model, image_path, class_names)
    return confidence_score


def webcam_predict_label(model, camera_index: int = 0, class_names: list = None) -> str:
    """
    Capture image from webcam and get only the predicted label.

    Parameters:
    model: The loaded Keras model object.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    str: The predicted label.
    """
    # Capture image from webcam
    image_path = capture_webcam_image(camera_index)

    # Make prediction using the model object
    predicted_class = predict_image_label(model, image_path, class_names)
    return predicted_class


def webcam_predict_confidence(model, camera_index: int = 0, class_names: list = None) -> float:
    """
    Capture image from webcam and get only the confidence score.

    Parameters:
    model: The loaded Keras model object.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    float: The confidence score.
    """
    # Capture image from webcam
    image_path = capture_webcam_image(camera_index)

    # Make prediction using the model object
    confidence_score = predict_image_confidence(model, image_path, class_names)
    return confidence_score


def predict_label_from_image(model, image_path: str, class_names: list = None) -> str:
    """
    Get predicted label from an existing image.

    Parameters:
    model: The loaded Keras model object.
    image_path (str): Path to the existing image file.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    str: The predicted label.
    """
    # Make prediction using the model object
    predicted_class = predict_image_label(model, image_path, class_names)
    return predicted_class


def predict_confidence_from_image(model, image_path: str, class_names: list = None) -> float:
    """
    Get predicted confidence from an existing image.

    Parameters:
    model: The loaded Keras model object.
    image_path (str): Path to the existing image file.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    float: The confidence score.
    """
    # Make prediction using the model object
    confidence_score = predict_image_confidence(model, image_path, class_names)
    return confidence_score


# --- RIMOSSE FUNZIONI LEGACY ---

# Elimina queste funzioni legacy:
# - webcam_predict_label_legacy
# - webcam_predict_confidence_legacy
# - webcam_predict

# --- FINE RIMOZIONE ---


def send_prediction_data(image_path: str, label: str, confidence: float, api_url: str, additional_data: dict = None) -> dict:
    """
    Send prediction data via REST API.

    Parameters:
    image_path (str): Path to the image file.
    label (str): Predicted label.
    confidence (float): Confidence score (0.0-1.0).
    api_url (str): URL of the REST API endpoint.
    additional_data (dict): Optional additional data to include in JSON.

    Returns:
    dict: API response or error information.
    """
    try:
        # Read and encode image as base64
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        # Create JSON payload (image only as base64, no image_path)
        payload = {
            "image": image_data,
            "label": label,
            "confidence": confidence,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Add additional data if provided
        if additional_data and isinstance(additional_data, dict):
            payload.update(additional_data)

        # Stampa la struttura del JSON che verrà inviato (senza stampare l'immagine base64)
        payload_preview = payload.copy()
        if "image" in payload_preview:
            payload_preview["image"] = f"<base64 string, length={len(payload['image'])}>"
        print("Struttura JSON inviata all'API:")
        print(json.dumps(payload_preview, indent=2))

        # Send POST request
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'MAST-Learn-CV-Module/2.0.0'
        }

        response = requests.post(
            api_url, json=payload, headers=headers, timeout=30)

        # Check response
        if response.status_code == 200:
            print(f"✅ Data sent successfully to {api_url}")
            try:
                return response.json()
            except:
                return {"status": "success", "message": "Data sent successfully", "response_text": response.text}
        else:
            error_msg = f"❌ API Error {response.status_code}: {response.text}"
            print(error_msg)
            return {"status": "error", "code": response.status_code, "message": response.text}

    except requests.exceptions.Timeout:
        error_msg = "❌ Request timeout - API took too long to respond"
        print(error_msg)
        return {"status": "error", "message": "Request timeout"}

    except requests.exceptions.ConnectionError:
        error_msg = f"❌ Connection error - Cannot reach {api_url}"
        print(error_msg)
        return {"status": "error", "message": "Connection error"}

    except FileNotFoundError:
        error_msg = f"❌ Image file not found: {image_path}"
        print(error_msg)
        return {"status": "error", "message": f"Image file not found: {image_path}"}

    except Exception as e:
        error_msg = f"❌ Unexpected error: {str(e)}"
        print(error_msg)
        return {"status": "error", "message": str(e)}


def webcam_predict_and_send(model, camera_index: int = 0, class_names: list = None, api_url: str = "", additional_data: dict = None) -> dict:
    """
    Complete workflow: capture image, predict, and send to API.

    Parameters:
    model: The loaded Keras model object.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.
    api_url (str): URL of the REST API endpoint.
    additional_data (dict): Optional additional data to include in JSON.

    Returns:
    dict: Combined prediction and API response data.
    """
    try:
        # Capture image from webcam
        image_path = capture_webcam_image(camera_index)

        # Make predictions
        label = predict_image_label(model, image_path, class_names)
        confidence = predict_image_confidence(model, image_path, class_names)

        # Send to API if URL provided
        api_response = None
        if api_url:
            api_response = send_prediction_data(
                image_path, label, confidence, api_url, additional_data)

        # Return combined results
        result = {
            "image_path": image_path,
            "label": label,
            "confidence": confidence,
            "api_sent": bool(api_url),
            "api_response": api_response
        }

        print(f"Prediction: {label} (confidence: {confidence:.2f})")
        if api_url:
            print(f"API Status: {api_response.get('status', 'unknown')}")

        return result

    except Exception as e:
        error_result = {
            "status": "error",
            "message": str(e),
            "label": None,
            "confidence": None,
            "api_sent": False,
            "api_response": None
        }
        print(f"❌ Workflow error: {str(e)}")
        return error_result


if __name__ == "__main__":
    # Test: cattura immagine da webcam, predizione da file esistente, invio dati a API
    try:
        # Parametri di test
        camera_index = 0
        model_path = "https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_ft.h5"
        class_names = ["aqualy", "calcolatrice_casio", "bicchiere", "iphone13",
                       "mouse_wireless", "pennarello_giotto", "persona", "webcam_box"]
        api_url = "https://petoiupload.vercel.app/api/predict"

        # Carica il modello
        model = load_custom_model(model_path)

        # 1. Cattura immagine da webcam
        image_path = capture_webcam_image(camera_index)

        # 2. Predizione label e confidenza da file esistente
        label = predict_label_from_image(model, image_path, class_names)
        confidence = predict_confidence_from_image(
            model, image_path, class_names)

        # 3. Invio dati alle API dedicate
        api_response = send_prediction_data(
            image_path, label, confidence, api_url)
        print(f"Risposta API: {api_response}")

    except Exception as e:
        print(f"Errore durante il test: {e}")

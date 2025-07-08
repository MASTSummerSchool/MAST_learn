import os
import platform
import cv2
import numpy as np
import urllib.request
import urllib.parse
from pathlib import Path

try:
    from keras.models import load_model
    from keras.preprocessing.image import img_to_array
    import keras.applications.mobilenet_v3
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

    # Save the captured image temporarily
    temp_path = compose_path("webcam_capture", ".jpg")
    cv2.imwrite(temp_path, frame)

    print(f"Immagine catturata e salvata in: {temp_path}")
    return temp_path


def load_custom_model(model_path: str = "mobilenet_NOME_v1.keras"):
    """
    Load a custom trained model from local file or URL.

    Parameters:
    model_path (str): Local filename or URL to the model file.
                     Examples:
                     - "my_model.keras" (local file)
                     - "https://github.com/user/repo/raw/main/model.keras" (URL)

    Returns:
    model: The loaded Keras model.
    """
    if not HAS_KERAS:
        raise ImportError(
            "Keras non è installato. Installare con: pip install keras")

    # Check if it's a URL
    if model_path.startswith(('http://', 'https://')):
        final_model_path = _download_model_from_url(model_path)
    else:
        # Local file - compose path
        final_model_path = _get_local_model_path(model_path)

    # Check if model exists
    if not os.path.exists(final_model_path):
        raise FileNotFoundError(f"Modello non trovato: {final_model_path}")

    # Load the model
    model = load_model(final_model_path)
    print(f"Modello caricato: {final_model_path}")

    return model


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
    model_dir = config_dir + sep + 'MAST_learn' + sep + 'test'
    
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
        raise RuntimeError(f"Errore durante il download del modello da {url}: {str(e)}")


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
    cache_dir = config_dir + sep + 'MAST_learn' + sep + 'models_cache'
    
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
    img_array = keras.applications.mobilenet_v3.preprocess_input(img_array)

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


def webcam_predict_label(model_name: str = "mobilenet_NOME_v1.keras", camera_index: int = 0, class_names: list = None) -> str:
    """
    Capture image from webcam and get only the predicted label.

    Parameters:
    model_name (str): Name of the model file.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    str: The predicted label.
    """
    predicted_class, _ = webcam_predict(model_name, camera_index, class_names)
    return predicted_class


def webcam_predict_confidence(model_name: str = "mobilenet_NOME_v1.keras", camera_index: int = 0, class_names: list = None) -> float:
    """
    Capture image from webcam and get only the confidence score.

    Parameters:
    model_name (str): Name of the model file.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    float: The confidence score.
    """
    _, confidence_score = webcam_predict(model_name, camera_index, class_names)
    return confidence_score


def webcam_predict(model_name: str = "mobilenet_NOME_v1.keras", camera_index: int = 0, class_names: list = None):
    """
    Capture image from webcam and predict using custom model.

    Parameters:
    model_name (str): Name of the model file.
    camera_index (int): Index of the camera to use.
    class_names (list): List of class names. If None, uses default classes.

    Returns:
    tuple: (predicted_class, confidence_score)
    """
    # Capture image from webcam
    image_path = capture_webcam_image(camera_index)

    # Load model
    model = load_custom_model(model_name)

    # Make prediction
    predicted_class, confidence_score = predict_image_custom(
        model, image_path, class_names)

    return predicted_class, confidence_score




if __name__ == "__main__":
    # Test the webcam prediction functionality
    try:
        result = webcam_predict()
        print(f"Risultato: {result}")
    except Exception as e:
        print(f"Errore durante il test: {e}")

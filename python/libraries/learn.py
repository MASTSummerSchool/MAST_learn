import os
import platform
import cv2
import numpy as np

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
        home_path = os.getenv('HomePath')
        config_dir = home_dir + home_path
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home

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
        raise RuntimeError(f"Impossibile accedere alla webcam con indice {camera_index}")
    
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


def load_custom_model(model_name: str = "mobilenet_NOME_v1.keras"):
    """
    Load a custom trained model.

    Parameters:
    model_name (str): Name of the model file.

    Returns:
    model: The loaded Keras model.
    """
    if not HAS_KERAS:
        raise ImportError("Keras non è installato. Installare con: pip install keras")
    
    # Compose path for the model
    if platform.system() == "Windows":
        sep = '\\'
        home_dir = os.getenv('HOMEDRIVE')
        home_path = os.getenv('HomePath')
        config_dir = home_dir + home_path
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home
    
    # Create the model directory path
    model_dir = config_dir + sep + 'MAST_learn' + sep + 'test'
    model_path = model_dir + sep + model_name
    
    # Check if model exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modello non trovato: {model_path}")
    
    # Load the model
    model = load_model(model_path)
    print(f"Modello caricato: {model_path}")
    
    return model


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
        raise ImportError("Keras non è installato. Installare con: pip install keras")
    
    # Use provided class names or default ones
    if class_names is None:
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
    predicted_class, confidence_score = predict_image_custom(model, image_path, class_names)
    
    return predicted_class, confidence_score


def create_class_list(*class_names):
    """
    Helper function to create a list of class names for prediction.

    Parameters:
    *class_names: Variable number of class name strings.

    Returns:
    list: List of class names.
    """
    return list(class_names)


if __name__ == "__main__":
    # Test the webcam prediction functionality
    try:
        result = webcam_predict()
        print(f"Risultato: {result}")
    except Exception as e:
        print(f"Errore durante il test: {e}")
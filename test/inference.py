import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# === Configurazione ===
MODEL_PATH = "test/mobilenet_NOME_v1.keras"  # Percorso del modello salvato
IMG_SIZE = (224, 224)  # Dimensione dell'immagine di input
CLASS_NAMES = [
    "aqualy", "calcolatrice_casio", "bicchiere", "iphone13", "mouse_wireless",
    "pennarello_giotto", "persona", "webcam_box"
]  # Classi del tuo dataset

# Percorso relativo dell'immagine (percorso statico)
IMG_PATH = "test/1.jpg"  # Sostituisci con il percorso dell'immagine

# Controlla che il modello esista
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modello non trovato: {MODEL_PATH}")

# === Caricamento del modello salvato ===
model = load_model(MODEL_PATH)


# === Funzione per fare inferenza su una singola immagine ===
def predict_image(img_path):
    # Carica e preprocessa l'immagine
    # Carica l'immagine e ridimensiona
    img = load_img(img_path, target_size=IMG_SIZE)
    # Converte l'immagine in un array numpy
    img_array = img_to_array(img)
    # Aggiungi la dimensione del batch (1, IMG_SIZE, IMG_SIZE, 3)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v3.preprocess_input(
        img_array)  # Preprocessing MobileNetV3

    # Previsione con il modello
    predictions = model.predict(img_array)

    # Calcola la probabilità e la classe predetta
    # Indice della classe con probabilità massima
    predicted_class_idx = np.argmax(predictions)
    predicted_class = CLASS_NAMES[predicted_class_idx]  # Nome della classe
    # Probabilità della classe predetta
    predicted_prob = predictions[0][predicted_class_idx]

    return predicted_class, predicted_prob


# === Esegui inferenza sulla singola immagine ===
if os.path.exists(IMG_PATH):  # Controlla che il file esista
    predicted_class, predicted_prob = predict_image(IMG_PATH)
    print(f"Classe predetta: {predicted_class}")
    print(f"Confidenza della predizione: {predicted_prob:.4f}")
else:
    print(f"Errore: L'immagine '{IMG_PATH}' non esiste.")

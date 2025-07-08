# MAST Learn Module

Modulo Python per Computer Vision con supporto a webcam, modelli Keras/TensorFlow, predizione e invio dati via REST API.

## Funzionalità principali

- **Cattura immagini** dalla webcam su Windows, Mac e Linux
- **Caricamento modelli** Keras/TensorFlow da file locale o URL
- **Predizione** di etichette e confidenza su immagini acquisite
- **Invio risultati** (inclusa immagine in base64) a endpoint REST API
- **Gestione classi personalizzate** per classificazione

## Installazione

1. Clona la repository:

   ```sh
   git clone https://github.com/MASTSummerSchool/MAST_learn.git
   cd MAST_learn
   ```

2. Installa le dipendenze Python:

   ```sh
   pip install -r requirements.txt
   ```

## Utilizzo

Esempio di utilizzo in `python/libraries/main.py`:

```python
from learn import webcam_predict_confidence, capture_webcam_image, webcam_predict_label, send_prediction_data, load_custom_model

camera_id = 1
image = capture_webcam_image(camera_id)
model_path = "https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5"
model = load_custom_model(model_path)
classes = ["aqualy","calcolatrice_casio","bicchiere","iphone13","mouse_wireless","pennarello_giotto","persona","webcam_box"]
label = webcam_predict_label(model, camera_id, classes)
confidence = webcam_predict_confidence(model, camera_id, classes)
send_api_url = "https://api.example.com/predict"
response = send_prediction_data(image, label, confidence, send_api_url)
print(response)
```

## Struttura della repository

- `python/libraries/learn.py` — Funzioni principali per CV, predizione e API
- `python/libraries/main.py` — Esempio di utilizzo
- `requirements.txt` — Dipendenze Python
- `config.json` — Configurazione moduli e dipendenze

## Requisiti

- Python 3.8+
- Webcam collegata e funzionante

## Licenza

LGPL

## Autore

Stefano Zingaro —

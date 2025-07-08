# Computer Vision Module for MAST Summer School

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Mind+](https://img.shields.io/badge/Mind+-Compatible-green.svg)](https://mindplus.dfrobot.com)
[![TensorFlow 2.11](https://img.shields.io/badge/TensorFlow-2.11-orange.svg)](https://tensorflow.org)
[![Educational](https://img.shields.io/badge/Purpose-Educational-purple.svg)](https://github.com/lozingaro/MAST_learn)

## 📋 Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Available Blocks](#available-blocks)
- [Supported Classes](#supported-classes)
- [File Structure](#file-structure)
- [Usage Examples](#usage-examples)
- [Technical Requirements](#technical-requirements)
- [API JSON Format](#api-json-format)
- [Webcam Configuration](#webcam-configuration)
- [Why Use Model Objects](#why-use-model-objects)
- [Educational Activities](#educational-activities)
- [Version](#version)
- [Contributing](#contributing)
- [License](#license)

## 📖 Description

Modulo di visione artificiale per la cattura di immagini da webcam e predizione di oggetti utilizzando modelli MobileNet custom. Progettato per attività didattiche di intelligenza artificiale e computer vision.

## Installazione

1. Scarica e installa [Mind+ Desktop app](https://mindplus.dfrobot.com)
2. Inserisci l'URL del progetto: **<https://github.com/lozingaro/MAST_learn>** nell'interfaccia per importare questa libreria

## Blocchi Disponibili (6 Blocchi Totali)

### 🎥 Cattura Webcam

- **`capture_webcam_image(camera_index)`** - Cattura un'immagine dalla webcam e la salva
  - `camera_index`: Indice della webcam (0 = webcam principale)
  - Restituisce: Percorso del file immagine salvato

### 🤖 Modello Custom  

- **`load_custom_model(model_path)`** - Carica un modello Keras personalizzato da file locale o URL
  - `model_path`: Nome del file modello o URL (es. "mobilenet_NOME_v1.keras" o "https://github.com/user/repo/raw/main/model.keras")
  - Restituisce: Modello caricato pronto per l'inferenza
  - ⭐ **Supporto URL**: Cache automatica per modelli remoti

### ⚡ Workflow Webcam Ottimizzato

- **`webcam_predict_label(model, camera_index, class_names)`** - ⭐ Cattura + predici etichetta
  - Usa oggetto model precaricato (più efficiente!)
  - Restituisce: Stringa con l'etichetta

- **`webcam_predict_confidence(model, camera_index, class_names)`** - ⭐ Cattura + predici confidenza  
  - Usa oggetto model precaricato (più efficiente!)
  - Restituisce: Numero decimale 0.0-1.0

### 🌐 API REST Integration

- **`send_prediction_data(image_path, label, confidence, api_url)`** - ⭐ Invia dati predizione via REST API
  - Codifica immagine in base64 e crea JSON con timestamp
  - Restituisce: Risposta API o informazioni errore

- **`webcam_predict_and_send(model, camera_index, class_names, api_url)`** - ⭐ Workflow completo con API
  - Cattura + predici + invia automaticamente all'API
  - Restituisce: Dati predizione combinati con risposta API

**Parametri comuni:**
- `model`: Oggetto modello caricato
- `camera_index`: Indice della webcam (0 = principale)
- `class_names`: Lista etichette (usa blocchi lista Mind+, opzionale)
- `api_url`: URL endpoint REST API (es. "https://api.example.com/predictions")

## Classi Supportate

Il modello custom MobileNet riconosce le seguenti 8 classi di oggetti:

- `aqualy` - Bottiglia d'acqua
- `calcolatrice_casio` - Calcolatrice Casio
- `bicchiere` - Bicchiere
- `iphone13` - iPhone 13
- `mouse_wireless` - Mouse wireless
- `pennarello_giotto` - Pennarello Giotto
- `persona` - Persona
- `webcam_box` - Scatola webcam

## Struttura File

```
~/models/
├── mobilenet_NOME_v1.keras        # Modelli locali
└── cache/
    └── downloaded_model.keras     # Modelli scaricati da URL

~/webcam_images/
├── webcam_capture_20250108_143025_123.jpg  # Immagini catturate con timestamp
├── webcam_capture_20250108_143030_456.jpg  # Non sovrascrive immagini precedenti
└── ...
```

## Esempio d'Uso

### ⭐ Workflow Semplificato (Predizione Base)

```python
# 1. Crea lista etichette con blocchi lista Mind+
mie_etichette = ["gatto", "cane", "uccello", "pesce", "coniglio", "tartaruga", "hamster", "criceto"]

# 2. Carica il modello UNA VOLTA (locale o da URL)
modello = load_custom_model("mio_modello_animali.keras")
# oppure da GitHub:
# modello = load_custom_model("https://github.com/utente/repo/raw/main/animali.keras")

# 3. Usa il modello precaricato per predizioni multiple (efficiente!)
etichetta = webcam_predict_label(modello, 0, mie_etichette)
print(f"Animale: {etichetta}")

# 4. Ottieni la confidenza con lo stesso modello
confidenza = webcam_predict_confidence(modello, 0, mie_etichette)
print(f"Sicurezza: {confidenza:.1%}")

# 5. Usa in condizioni Mind+
if etichetta == "gatto":
    print("Miao!")
if confidenza > 0.8:
    print("Predizione molto sicura!")
```

### 🌐 Workflow con API REST (Nuovo!)

```python
# 1. Setup modello e classi
mie_etichette = ["gatto", "cane", "uccello", "pesce", "coniglio", "tartaruga", "hamster", "criceto"]
modello = load_custom_model("mio_modello_animali.keras")

# 2. Workflow completo con invio automatico API
api_url = "https://mia-api.com/predictions"
risultato = webcam_predict_and_send(modello, 0, mie_etichette, api_url)

print(f"Predizione: {risultato['label']} ({risultato['confidence']:.2f})")
print(f"API Status: {risultato['api_response']['status']}")

# 3. Oppure invio manuale separato
immagine = capture_webcam_image(0)
etichetta = webcam_predict_label(modello, 0, mie_etichette)
confidenza = webcam_predict_confidence(modello, 0, mie_etichette)

# Invia dati all'API
api_response = send_prediction_data(immagine, etichetta, confidenza, api_url)
print(f"API Response: {api_response}")
```

### Workflow Manuale (Separato)

```python
# 1. Cattura immagine separatamente
immagine = capture_webcam_image(0)

# 2. Carica modello (locale o da URL)
modello = load_custom_model("mio_modello.keras")
# oppure da GitHub:
# modello = load_custom_model("https://github.com/utente/repo/raw/main/modello.keras")

# 3. Crea etichette custom con blocchi lista Mind+
etichette = ["classe1", "classe2", "classe3", "classe4", "classe5", "classe6", "classe7", "classe8"]

# 4. Usa l'immagine catturata manualmente
# (Nota: per immagini pre-catturate, serve una funzione predict_image separata)
```

## Requisiti Tecnici

### Dipendenze Principali (Python 3.8+ compatibili)
- **numpy** >= 1.19.5 - Operazioni array e calcoli numerici
- **opencv-python** >= 4.5.0 - Cattura e elaborazione immagini webcam
- **tensorflow** >= 2.8.0, <2.16.0 - TensorFlow compatibile con Python 3.8
- **keras** >= 2.8.0, <3.0.0 - Caricamento modelli e inferenza (TF.Keras)

### Dipendenze di Supporto
- **requests** >= 2.25.0 - Comunicazioni HTTP per API REST
- **h5py** >= 3.1.0 - Lettura/scrittura file modelli HDF5
- **six** >= 1.15.0 - Compatibilità Python 2/3
- **protobuf** >= 3.19.0, <4.0.0 - Serializzazione dati TensorFlow
- **typing-extensions** >= 3.7.4 - Supporto type hints

⚡ **Nota**: Dipendenze ottimizzate per Mind+ Python 3.8.5 - configurazione manuale completa!

### 🎯 Compatibilità Mind+
- **Python 3.8.5** - Versione target per ambiente Mind+
- **TensorFlow 2.11.1** - Stabile e compatibile con Python 3.8
- **Keras 2.11.0** - Integrato in TensorFlow (tensorflow.keras)
- **Protobuf <4.0** - Evita conflitti di versione
- **Installazione automatica** - Mind+ gestisce tutte le dipendenze

## Formato JSON API

### Payload inviato all'API REST

```json
{
  "image": "base64_encoded_image_data...",
  "label": "gatto",
  "confidence": 0.94,
  "timestamp": "2025-01-08T14:30:15.123456",
  "image_path": "webcam_capture.jpg"
}
```

### Headers HTTP automatici

```http
Content-Type: application/json
User-Agent: MAST-Learn-CV-Module/2.0.0
```

### Gestione errori automatica

```json
// Successo (200 OK)
{
  "status": "success",
  "message": "Data received successfully",
  "id": "prediction-12345"
}

// Errore di connessione
{
  "status": "error",
  "message": "Connection error"
}

// Timeout API
{
  "status": "error", 
  "message": "Request timeout"
}
```

## Configurazione Webcam

- **Indice 0**: Webcam principale/integrata
- **Indice 1**: Prima webcam esterna USB
- **Indice 2**: Seconda webcam esterna USB

## Attività Didattiche

### Computer Vision Hands-On

1. **Setup**: Installazione dipendenze e configurazione webcam
2. **Cattura**: Acquisizione immagini di oggetti diversi
3. **Inferenza**: Caricamento modello e predizione oggetti
4. **Analisi**: Interpretazione confidence score e accuratezza
5. **Esperimenti**: Test con oggetti diversi e condizioni di luce

## Vantaggi Approccio Efficiente

### 🚀 Perché usare l'oggetto model?

**Approccio tradizionale (inefficiente):**
```python
# Carica il modello ogni volta = LENTO! ⚠️
etichetta1 = webcam_predict_label("modello.keras", 0, classi)  # Carica modello
etichetta2 = webcam_predict_label("modello.keras", 0, classi)  # Carica ANCORA
etichetta3 = webcam_predict_label("modello.keras", 0, classi)  # Carica ANCORA
```

**Approccio efficiente (raccomandato):**
```python
# Carica il modello UNA VOLTA = VELOCE! ✅
modello = load_custom_model("modello.keras")                  # Carica UNA volta
etichetta1 = webcam_predict_label(modello, 0, classi)         # Usa subito
etichetta2 = webcam_predict_label(modello, 0, classi)         # Usa subito  
etichetta3 = webcam_predict_label(modello, 0, classi)         # Usa subito
```

**Risultato:** Tempo di esecuzione ridotto del 70-80%! ⚡

## Versione

**v2.1.2** - Modulo Computer Vision con organizzazione migliorata: gestione file ottimizzata, documentazione completa e repository standards

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Educational Use
This software is developed for educational purposes as part of the MAST (Machine Learning, Artificial Intelligence, Statistics) Summer School program at the University of Bologna.

## 📧 Contact

- **Author**: Stefano Zingaro
- **Email**: stefano.zingaro@unibo.it
- **Institution**: University of Bologna
- **Project**: MAST Summer School

## 🙏 Acknowledgments

- University of Bologna MAST Summer School Program
- Mind+ Development Team for the visual programming platform
- TensorFlow and OpenCV communities for robust ML and CV libraries
- All students and educators who provide feedback to improve this educational tool

# Computer Vision Module for MAST Summer School

## Descrizione

Modulo di visione artificiale per la cattura di immagini da webcam e predizione di oggetti utilizzando modelli MobileNet custom. Progettato per attività didattiche di intelligenza artificiale e computer vision.

## Installazione

1. Scarica e installa [Mind+ Desktop app](https://mindplus.dfrobot.com)
2. Inserisci l'URL del progetto: **<https://github.com/lozingaro/MAST_learn>** nell'interfaccia per importare questa libreria

## Blocchi Disponibili (4 Blocchi Essenziali)

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

**Parametri comuni:**
- `model`: Oggetto modello caricato
- `camera_index`: Indice della webcam (0 = principale)
- `class_names`: Lista etichette (usa blocchi lista Mind+, opzionale)

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
~/MAST_learn/
├── test/
│   └── mobilenet_NOME_v1.keras    # Modelli locali
└── models_cache/
    └── downloaded_model.keras     # Modelli scaricati da URL

~/webcam_images/
└── webcam_capture.jpg             # Immagini catturate
```

## Esempio d'Uso

### ⭐ Workflow Semplificato (4 Blocchi)

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

### Dipendenze Principali
- **numpy** >= 1.24.3 - Operazioni array e calcoli numerici
- **opencv-python** >= 4.7.0 - Cattura e elaborazione immagini webcam
- **tf-nightly** >= 2.20.0 - TensorFlow nightly (supporta Python 3.13+)
- **keras** >= 3.10.0 - Caricamento modelli e inferenza

### Dipendenze TensorFlow (configurate automaticamente)
- **absl-py**, **astunparse**, **flatbuffers**, **gast**, **google-pasta**
- **grpcio**, **h5py**, **libclang**, **markdown**, **ml-dtypes**
- **opt-einsum**, **packaging**, **protobuf**, **requests**, **setuptools**
- **six**, **tensorboard**, **tensorboard-data-server**, **termcolor**
- **typing-extensions**, **urllib3**, **werkzeug**, **wrapt**

⚡ **Nota**: Tutte le dipendenze sono configurate manualmente in config.json per evitare problemi con pipreqs!

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

**v2.0.0** - Modulo Computer Vision semplificato con 4 blocchi essenziali: cattura webcam, carica modello, predici label e confidence

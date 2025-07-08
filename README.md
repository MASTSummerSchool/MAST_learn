# Computer Vision Module for MAST Summer School

## Descrizione

Modulo di visione artificiale per la cattura di immagini da webcam e predizione di oggetti utilizzando modelli MobileNet custom. Progettato per attività didattiche di intelligenza artificiale e computer vision.

## Installazione

1. Scarica e installa [Mind+ Desktop app](https://mindplus.dfrobot.com)
2. Inserisci l'URL del progetto: **<https://github.com/lozingaro/MAST_learn>** nell'interfaccia per importare questa libreria

## Blocchi Disponibili

### 🎥 Cattura Webcam

- **`capture_webcam_image(camera_index)`** - Cattura un'immagine dalla webcam e la salva
  - `camera_index`: Indice della webcam (0 = webcam principale)
  - Restituisce: Percorso del file immagine salvato

### 🤖 Modello Custom  

- **`load_custom_model(model_path)`** - Carica un modello Keras personalizzato da file locale o URL
  - `model_path`: Nome del file modello o URL (es. "mobilenet_NOME_v1.keras" o "https://github.com/user/repo/raw/main/model.keras")
  - Restituisce: Modello caricato pronto per l'inferenza
  - ⭐ **Nuovo**: Supporto URL con cache automatica

### 🔍 Predizione Immagine

- **`predict_image_custom(model, image_path, class_names)`** - Predice oggetto e confidenza da immagine
  - Restituisce: Tupla (etichetta_predetta, punteggio_confidenza)

- **`predict_image_label(model, image_path, class_names)`** - ⭐ Ottieni solo l'etichetta predetta
  - Restituisce: Stringa con l'etichetta (es. "gatto")

- **`predict_image_confidence(model, image_path, class_names)`** - ⭐ Ottieni solo il punteggio di confidenza  
  - Restituisce: Numero decimale 0.0-1.0 (es. 0.87)

### ⚡ Workflow Webcam Efficiente

- **`webcam_predict_label(model, camera_index, class_names)`** - ⭐ Cattura + predici etichetta
  - Usa oggetto model precaricato (più efficiente!)
  - Restituisce: Stringa con l'etichetta

- **`webcam_predict_confidence(model, camera_index, class_names)`** - ⭐ Cattura + predici confidenza  
  - Usa oggetto model precaricato (più efficiente!)
  - Restituisce: Numero decimale 0.0-1.0

- **`webcam_predict(model_name, camera_index, class_names)`** - Workflow legacy
  - Carica modello ogni volta (meno efficiente)
  - Restituisce: Tupla (etichetta_predetta, punteggio_confidenza)

**Parametri comuni:**
- `model/model_name`: Modello caricato / Nome del file modello o URL
- `image_path`: Percorso del file immagine  
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

### ⭐ Approccio Efficiente (Raccomandato)

```python
# 1. Crea lista etichette con blocchi lista Mind+
mie_etichette = ["gatto", "cane", "uccello", "pesce", "coniglio", "tartaruga", "hamster", "criceto"]

# 2. Carica il modello UNA VOLTA (locale o da URL)
modello = load_custom_model("mio_modello_animali.keras")
# oppure da GitHub:
# modello = load_custom_model("https://github.com/utente/repo/raw/main/animali.keras")

# 3. Usa il modello precaricato (più veloce!)
etichetta = webcam_predict_label(modello, 0, mie_etichette)
print(f"Animale: {etichetta}")

# 4. Ottieni solo la confidenza con lo stesso modello
confidenza = webcam_predict_confidence(modello, 0, mie_etichette)
print(f"Sicurezza: {confidenza:.1%}")

# 5. Usa in condizioni Mind+
if etichetta == "gatto":
    print("Miao!")
if confidenza > 0.8:
    print("Predizione molto sicura!")
```

### Con Etichette Custom (Tupla)

```python
# Metodo tradizionale (restituisce tupla)
risultato = webcam_predict("mio_modello_animali.keras", 0, mie_etichette)
etichetta, confidenza = risultato
print(f"Animale rilevato: {etichetta} ({confidenza:.2f})")
```

### Con Etichette Default  

```python
# Usa le etichette di default (aqualy, calcolatrice_casio, ecc.)
risultato = webcam_predict("mobilenet_NOME_v1.keras", 0, None)
etichetta, confidenza = risultato
print(f"Oggetto: {etichetta} ({confidenza:.2f})")
```

### Workflow Manuale

```python
# 1. Cattura immagine
immagine = capture_webcam_image(0)

# 2. Carica modello (locale o da URL)
modello = load_custom_model("mio_modello.keras")
# oppure da GitHub:
# modello = load_custom_model("https://github.com/utente/repo/raw/main/modello.keras")

# 3. Crea etichette custom con blocchi lista Mind+
etichette = ["classe1", "classe2", "classe3", "classe4", "classe5", "classe6", "classe7", "classe8"]

# 4. Predici
etichetta, confidenza = predict_image_custom(modello, immagine, etichette)
print(f"Predizione: {etichetta}, Confidenza: {confidenza:.2f}")
```

## Requisiti Tecnici

- **opencv-python** >= 4.7.0 - Cattura e elaborazione immagini  
- **tf-nightly** - TensorFlow nightly con Keras 3.10+ integrato (supporta Python 3.13+)
- **numpy** >= 1.24.0 - Operazioni array

⚡ **Nota**: Usa TensorFlow nightly per compatibilità Python 3.13+ con preprocessing MobileNet ottimizzato!

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

**v1.1.0** - Modulo Computer Vision ottimizzato con supporto URL e workflow efficiente con oggetti model

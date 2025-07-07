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
- **`load_custom_model(model_name)`** - Carica un modello Keras personalizzato
  - `model_name`: Nome del file modello (es. "mobilenet_NOME_v1.keras")
  - Restituisce: Modello caricato pronto per l'inferenza

### 🏷️ Etichette Custom
- **`create_class_list(class1, class2, ..., class8)`** - Crea lista etichette personalizzate
  - `class1-8`: Le etichette del tuo modello (in ordine di training)
  - Restituisce: Lista di etichette da usare per la predizione

### 🔍 Predizione Immagine
- **`predict_image_custom(model, image_path, class_names)`** - Predice oggetto e confidenza da immagine
  - `model`: Modello caricato con `load_custom_model`
  - `image_path`: Percorso del file immagine
  - `class_names`: Lista etichette (opzionale, usa default se None)
  - Restituisce: Tupla (etichetta_predetta, punteggio_confidenza)

### ⚡ Workflow Completo
- **`webcam_predict(model_name, camera_index, class_names)`** - Cattura + carica modello + predice
  - `model_name`: Nome del file modello
  - `camera_index`: Indice della webcam
  - `class_names`: Lista etichette (opzionale, usa default se None)
  - Restituisce: Tupla (etichetta_predetta, punteggio_confidenza)

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
└── test/
    └── mobilenet_NOME_v1.keras    # Modello custom

~/webcam_images/
└── webcam_capture.jpg             # Immagini catturate
```

## Esempio d'Uso

### Con Etichette Custom
```python
# 1. Definisci le tue etichette (nell'ordine del training!)
mie_etichette = create_class_list("gatto", "cane", "uccello", "pesce", "coniglio", "tartaruga", "hamster", "criceto")

# 2. Cattura e predici con etichette custom
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

# 2. Carica modello  
modello = load_custom_model("mio_modello.keras")

# 3. Crea etichette custom
etichette = create_class_list("classe1", "classe2", "classe3", "classe4", "classe5", "classe6", "classe7", "classe8")

# 4. Predici
etichetta, confidenza = predict_image_custom(modello, immagine, etichette)
print(f"Predizione: {etichetta}, Confidenza: {confidenza:.2f}")
```

## Requisiti Tecnici

- **opencv-python** >= 4.5.0 - Cattura e elaborazione immagini
- **keras** >= 2.8.0 - Caricamento e inferenza modello
- **numpy** >= 1.20.0 - Operazioni array

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

## Versione

**v1.0.0** - Modulo Computer Vision dedicato con 4 blocchi per webcam e inferenza modelli custom MobileNet
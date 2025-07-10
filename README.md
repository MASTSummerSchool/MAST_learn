# MAST Learn - Computer Vision Made Simple 🎯

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Mind+](https://img.shields.io/badge/Mind+-Compatible-green.svg)](https://mindplus.dfrobot.com)
[![TensorFlow 2.11](https://img.shields.io/badge/TensorFlow-2.11-orange.svg)](https://tensorflow.org)
[![Educational](https://img.shields.io/badge/Purpose-Educational-purple.svg)](https://github.com/lozingaro/MAST_learn)

## 🎯 What is MAST Learn?

MAST Learn è un modulo di computer vision pensato per chi vuole imparare l'intelligenza artificiale in modo pratico e divertente. Sviluppato per la MAST Summer School dell'Università di Bologna, ti permette di:

- **Catturare immagini dalla webcam** con un semplice click
- **Riconoscere oggetti** usando modelli di intelligenza artificiale
- **Condividere le tue predizioni** attraverso API web
- **Imparare facendo** con esempi pratici e intuitivi

Perfetto per studenti, insegnanti e chiunque voglia scoprire il mondo della computer vision senza dover diventare un esperto di programmazione!

## 📋 Indice

- [Installazione Quick Start](#installazione-quick-start)
- [Funzioni Disponibili](#funzioni-disponibili)
- [Esempi Pratici](#esempi-pratici)
- [Classi Riconosciute](#classi-riconosciute)
- [Risoluzione Problemi](#risoluzione-problemi)
- [Per Sviluppatori](#per-sviluppatori)
- [Licenza e Contatti](#licenza-e-contatti)

## 🚀 Installazione Quick Start

**Hai 2 minuti? Ecco come iniziare:**

1. **Scarica Mind+**: Vai su [mindplus.dfrobot.com](https://mindplus.dfrobot.com) e installa l'app
2. **Importa MAST Learn**: Copia e incolla questo URL: `https://github.com/lozingaro/MAST_learn`
3. **Inizia a sperimentare**: Sei pronto! Le dipendenze si installano automaticamente

## 🛠️ Funzioni Disponibili

MAST Learn offre **23 funzioni** organizzate in 5 categorie principali. Ecco le più importanti che userai:

### 🎥 **Cattura Immagini** (Le Basi)

**`capture_webcam_image(camera_index=0)`** 📸
- Scatta una foto con la webcam e la salva automaticamente
- Perfetto per iniziare - funziona subito!
- *Restituisce*: Il percorso dove è salvata l'immagine

### 🤖 **Gestione Modelli** (Il Motore)

**`load_custom_model(model_path)`** 🧠
- Carica il "cervello" dell'intelligenza artificiale
- Supporta modelli da file locali, percorsi personalizzati o da internet
- *Trucco*: Carica una volta, usa tante volte (molto più veloce!)
- *Bonus*: Converte automaticamente i formati problematici

**Dove mettere i tuoi modelli:**
- **Windows**: `C:\Users\TuoNome\models\mio_modello.h5`
- **Mac**: `/Users/TuoNome/models/mio_modello.h5`
- **Linux**: `/home/TuoNome/models/mio_modello.h5`
- **Personalizzato**: Qualsiasi percorso completo che vuoi!
- **Online**: URL diretti da GitHub o altri server

### ⚡ **Predizioni Webcam** (La Magia)

**`webcam_predict_label(model, camera_index, class_names)`** 🎯
- Scatta una foto E riconosce l'oggetto in un colpo solo
- *Restituisce*: Il nome dell'oggetto riconosciuto

**`webcam_predict_confidence(model, camera_index, class_names)`** 📊
- Come sopra, ma ti dice quanto è sicuro (da 0.0 a 1.0)
- *Perfetto per*: Capire se fidarsi della predizione

### 🆕 **Predizioni su Immagini Esistenti** (Novità!)

**`predict_label_from_image(model, image_path, class_names)`** 🔍
- Riconosce oggetti in immagini già salvate
- *Ideale per*: Analizzare la stessa foto più volte

**`predict_confidence_from_image(model, image_path, class_names)`** 📈
- Come sopra, ma restituisce il livello di confidenza
- *Perfetto per*: Confrontare predizioni sulla stessa immagine

### 🌐 **Condivisione Online** (Per i Social!)

**`send_prediction_data(image_path, label, confidence, api_url)`** 📤
- Invia le tue scoperte a un server web
- *Utile per*: Creare app web o condividere risultati

**`webcam_predict_and_send(model, camera_index, class_names, api_url)`** 🚀
- Fa tutto in automatico: scatta, riconosce, invia!
- *Perfetto per*: Progetti avanzati o demo live

### 🔧 **Risoluzione Problemi** (Il Pronto Soccorso)

**`verify_model_compatibility(model_path)`** 🩺
- Controlla se il tuo modello funziona correttamente
- *Utile quando*: Qualcosa non va e non sai perché

**`convert_model_format(input_path, output_path, target_format)`** 🔄
- Converte modelli tra formati diversi
- *Salva-vita per*: Modelli che danno errori strani

## 🧪 Esempi Pratici

### 🎯 **Esempio 1: Il tuo primo riconoscimento oggetti**

```python
# Passo 1: Carica il modello (solo una volta!)
# Opzioni diverse per caricare modelli:

# A) Modello MAST-AI ufficiale (default, consigliato!)
modello = load_custom_model("https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5")

# B) Modello locale (metti il tuo file nella cartella models)
# modello = load_custom_model("mio_modello.h5")

# C) Percorso personalizzato completo
# Windows: modello = load_custom_model(r"C:\Users\TuoNome\Desktop\modelli\mio_modello.h5")
# Mac:     modello = load_custom_model("/Users/TuoNome/Desktop/modelli/mio_modello.h5")
# Linux:   modello = load_custom_model("/home/TuoNome/Desktop/modelli/mio_modello.h5")

# Passo 2: Definisci cosa può riconoscere
oggetti = ["aqualy", "calcolatrice_casio", "bicchiere", "iphone13", "mouse_wireless", "pennarello_giotto", "persona", "webcam_box"]

# Passo 3: Scatta e riconosci!
cosa_vedo = webcam_predict_label(modello, 0, oggetti)
quanto_sicuro = webcam_predict_confidence(modello, 0, oggetti)

# Passo 4: Mostra i risultati
print(f"Ho visto: {cosa_vedo}")
print(f"Sono sicuro al {quanto_sicuro:.1%}")
```

### 🔍 **Esempio 2: Analizza la stessa foto più volte (NUOVO!)**

```python
# Scatta una foto una volta sola
foto = capture_webcam_image(0)

# Analizzala con diversi modelli o impostazioni
cosa_vedo = predict_label_from_image(modello, foto, oggetti)
sicurezza = predict_confidence_from_image(modello, foto, oggetti)

print(f"Nella foto vedo: {cosa_vedo} (sicurezza: {sicurezza:.1%})")

# Bonus: Puoi rianalizzare la stessa foto quando vuoi!
# Utile per confrontare risultati o per lezioni
```

### 🌐 **Esempio 3: Condividi online le tue scoperte**

```python
# Setup iniziale con diversi modi di caricare modelli
# Opzione 1: Modello MAST-AI ufficiale
modello = load_custom_model("https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5")

# Opzione 2: Modello personalizzato
# modello = load_custom_model("mio_modello_animali.h5")

# Opzione 3: Percorso completo personalizzato
# modello = load_custom_model("/percorso/completo/al/mio/modello.h5")

oggetti = ["gatto", "cane", "uccello", "pesce"]

# Condivisione automatica
risultato = webcam_predict_and_send(modello, 0, oggetti, "https://petoiupload.vercel.app/api/predict")

print(f"Ho riconosciuto: {risultato['label']}")
print(f"Inviato al server: {risultato['api_response']['status']}")
```

### 🎓 **Esempio 4: Per insegnanti - Workflow didattico**

```python
# Perfetto per lezioni interattive!
# Scegli come caricare il modello:

# A) Modello MAST-AI ufficiale (pronto all'uso!)
modello = load_custom_model("https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5")
oggetti_scuola = ["aqualy", "calcolatrice_casio", "bicchiere", "iphone13", "mouse_wireless", "pennarello_giotto", "persona", "webcam_box"]

# B) Il tuo modello personalizzato
# modello = load_custom_model("oggetti_scuola.h5")  # Nella cartella ~/models/
# oggetti_scuola = ["penna", "libro", "quaderno", "gomma", "righello"]

# C) Percorso completo personalizzato
# modello = load_custom_model("C:\\Users\\Insegnante\\Desktop\\modelli\\scuola.h5")  # Windows
# modello = load_custom_model("/Users/Insegnante/Desktop/modelli/scuola.h5")        # Mac
# modello = load_custom_model("/home/insegnante/Desktop/modelli/scuola.h5")         # Linux

# Gli studenti mostrano oggetti alla webcam
for tentativo in range(5):
    input("Premi INVIO quando hai un oggetto davanti alla webcam...")
    
    oggetto = webcam_predict_label(modello, 0, oggetti_scuola)
    confidenza = webcam_predict_confidence(modello, 0, oggetti_scuola)
    
    print(f"Tentativo {tentativo + 1}: {oggetto} (confidenza: {confidenza:.1%})")
    
    if confidenza > 0.8:
        print("🎉 Ottimo! Predizione molto sicura!")
    else:
        print("🤔 Prova a migliorare l'inquadratura...")
```

## 🎯 Classi Riconosciute

Il modello principale di MAST Learn riconosce questi **8 oggetti comuni**:

| Oggetto | Descrizione | Emoji |
|---------|-------------|--------|
| `aqualy` | Bottiglia d'acqua | 💧 |
| `calcolatrice_casio` | Calcolatrice Casio | 🔢 |
| `bicchiere` | Bicchiere | 🥤 |
| `iphone13` | iPhone 13 | 📱 |
| `mouse_wireless` | Mouse wireless | 🖱️ |
| `pennarello_giotto` | Pennarello Giotto | 🖊️ |
| `persona` | Persona | 👤 |
| `webcam_box` | Scatola webcam | 📦 |

> **Nota per insegnanti**: Puoi usare i tuoi modelli personalizzati con qualsiasi classe! Questi sono solo gli esempi inclusi.

## 📁 Configurazione Modelli e File

### 🎯 **Come Caricare i Modelli** (Importante!)

MAST Learn ti offre **3 modi** per caricare i modelli:

#### **1. Modello MAST-AI Ufficiale** (Consigliato! 🌟)
```python
# Usa il modello già pronto del progetto MAST-AI
modello = load_custom_model("https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5")
```
**Vantaggi**: Sempre aggiornato, funziona subito, riconosce 8 oggetti comuni

#### **2. Modello Locale** (Semplice)
```python
# Metti il tuo file nella cartella ~/models/ e usa solo il nome
modello = load_custom_model("mio_modello.h5")
```
**Percorsi automatici**:
- **Windows**: `C:\Users\TuoNome\models\mio_modello.h5`
- **Mac**: `/Users/TuoNome/models/mio_modello.h5`
- **Linux**: `/home/TuoNome/models/mio_modello.h5`

#### **3. Percorso Personalizzato** (Massima Flessibilità)
```python
# Specifica il percorso completo dove vuoi tu
# Windows
modello = load_custom_model(r"C:\Users\TuoNome\Desktop\progetti\modelli\mio_modello.h5")

# Mac
modello = load_custom_model("/Users/TuoNome/Desktop/progetti/modelli/mio_modello.h5")

# Linux
modello = load_custom_model("/home/TuoNome/Desktop/progetti/modelli/mio_modello.h5")
```

### 📂 **Dove Finiscono i File**

```
📂 La tua home directory
├── 📁 models/                     # I tuoi modelli AI
│   ├── 🧠 mio_modello.keras       # Modelli originali
│   ├── 🔄 mio_modello_convertito.h5  # Conversioni automatiche
│   └── 📁 cache/                  # Modelli scaricati da internet
│       └── 💾 modello_online.h5
└── 📁 webcam_images/              # Le tue foto
    ├── 📷 foto_20250710_143025.jpg
    ├── 📷 foto_20250710_143030.jpg
    └── 📷 ...
```

> **Tip**: Su Windows è `C:\Users\TuoNome\`, su Mac è `/Users/TuoNome/`, su Linux è `/home/TuoNome/`

## 🆘 Risoluzione Problemi

### "Il mio modello non funziona!" 😫

**Respira! È normale.** Ecco la soluzione in 3 passi:

#### **Passo 1: Diagnosi automatica**
```python
# Lascia che MAST Learn controlli cosa non va
info = verify_model_compatibility("mio_modello.keras")
print(info)
```

#### **Passo 2: Conversione automatica**
```python
# MAST Learn prova a sistemare automaticamente
modello = load_custom_model("mio_modello.keras")
# Se vedi "🔄 Conversione automatica..." sei a posto!
```

#### **Passo 3: Se ancora non funziona**
```python
# Forza la conversione manuale
modello_sistemato = convert_model_format("mio_modello.keras", target_format="h5")
modello = load_custom_model(modello_sistemato)
```

### "La webcam non funziona!" 📷

```python
# Prova webcam diverse
foto = capture_webcam_image(0)  # Webcam principale
# oppure
foto = capture_webcam_image(1)  # Webcam esterna
```

### "Le predizioni sono sbagliate!" 🤔

- **Controlla la luce**: Serve buona illuminazione
- **Avvicina l'oggetto**: Riempi il frame
- **Controlla le classi**: Stai usando la lista giusta?
- **Verifica la confidenza**: Se sotto 0.7, prova a migliorare l'inquadratura

### Problemi Comuni e Fix Rapidi

| Problema | Soluzione Rapida |
|----------|------------------|
| "File not found" | Controlla che il file sia in `~/models/` |
| "Camera not found" | Prova `camera_index=1` o `2` |
| "Low confidence" | Migliora illuminazione e inquadratura |
| "Wrong predictions" | Verifica di usare la lista classi corretta |
| "Import error" | Riavvia Mind+ e riprova |

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

## 🔧 Per Sviluppatori

### Struttura del Progetto

```
MAST_learn/
├── python/
│   └── libraries/
│       ├── learn.py       # 🧠 Tutte le funzioni principali
│       └── main.py        # 📝 Esempi pratici
├── config.json           # ⚙️ Configurazione Mind+
└── README.md             # 📚 Questa guida
```

### Requisiti Tecnici

- **Python 3.8+** (ottimizzato per Mind+)
- **TensorFlow 2.8-2.15** (no TF 2.16+)
- **OpenCV 4.5+** per webcam
- **NumPy, Requests** per il resto

> **Nota**: Mind+ installa tutto automaticamente, non preoccuparti!

### Come Contribuire

Hai un'idea per migliorare MAST Learn? Fantastico! 

1. **Fai un fork** del progetto
2. **Crea un branch** per la tua feature: `git checkout -b feature/idea-geniale`
3. **Fai le tue modifiche** e testale
4. **Invia una pull request** con una descrizione chiara

### Testare le Modifiche

```python
# Test rapido delle funzioni base
modello = load_custom_model("https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5")
foto = capture_webcam_image(0)
risultato = predict_label_from_image(modello, foto, ["test"])
print(f"Funziona: {risultato}")
```

## 📄 Licenza e Contatti

### Licenza
Questo progetto è rilasciato sotto **licenza MIT** - puoi usarlo, modificarlo e condividerlo liberamente!

### Chi Siamo
- **Autore**: Prof. Stefano Zingaro
- **Email**: stefano.zingaro@unibo.it
- **Università**: Università di Bologna
- **Progetto**: MAST Summer School

### Ringraziamenti 💙
- **Università di Bologna** per la MAST Summer School
- **Tutti gli studenti** che hanno testato e migliorato questo strumento
- **Mind+ Team** per la piattaforma di programmazione visuale
- **TensorFlow e OpenCV** per le librerie robuste
- **La community open source** per l'ispirazione continua

---

## 🎯 Versione Attuale

**v2.3.0** - Funzioni per immagini esistenti + README umanizzato

### Novità
- ✨ Nuove funzioni `predict_label_from_image()` e `predict_confidence_from_image()`
- 📚 README completamente riscritto in stile umano
- 🔧 Esempi pratici e guide per principianti
- 🎓 Sezioni dedicate per insegnanti

### Prossimi Obiettivi
- 🌟 Supporto per modelli YOLO (object detection)
- 🎨 Interfaccia grafica per Mind+
- 🔊 Integrazione con text-to-speech
- 🌐 Più esempi di integrazione API

---

*Fatto con ❤️ per la comunità educativa italiana*

# Machine Learning library for the MAST summer school

## How to install

Download and install [Mind+ Desktop app](https://mindplus.dfrobot.com).

Input the project URL: **<https://github.com/lozingaro/MAST_learn>** in the interface to import this library.

## Proposta Attività Didattiche Hands-On per la Scuola Estiva su IoT e AI

### Hands-On 1: Introduzione al Machine Learning
Insegnare agli studenti le basi del machine learning, con una spiegazione dei diversi tipi di apprendimento automatico e un focus sull'apprendimento supervisionato tramite attività di laboratorio.

### Hands-On 2: Alberi Decisionali
Insegnare agli studenti come funzionano gli alberi decisionali e come implementarli per i compiti di classificazione attraverso un'attività unplugged e di laboratorio.

### Hands-On 3: Reti Neurali
Introdurre agli studenti le reti neurali e la loro applicazione in compiti di classificazione più complessi.

### Hands-On 4: Classificazione in Tempo Reale con Bittle (Progetto Finale)
Applicare i modelli addestrati per classificare i movimenti di Bittle in tempo reale, utilizzando anche la visione artificiale per riconoscimento di oggetti.

## Blocchi Disponibili

### Blocchi di Addestramento

- `train_decision_tree(filename)`: Addestra un modello di albero decisionale dai dati CSV
- `train_neural_network(filename)`: Addestra un modello di rete neurale dai dati CSV

### Blocchi di Predizione

- `infer(model, data)`: Effettua predizioni usando un modello addestrato (restituisce la label più comune)
- `get_label(model, data)`: Ottiene la label predetta per un singolo punto dati
- `get_confidence_score(model, data)`: Ottiene il punteggio di confidenza (probabilità) per una predizione

### Blocchi di Visione Artificiale

- `capture_webcam_image(camera_index)`: Cattura un'immagine dalla webcam e la salva
- `load_custom_model(model_name)`: Carica un modello TensorFlow custom addestrato
- `predict_image_custom(model, image_path)`: Predice l'etichetta e il punteggio di confidenza per un'immagine
- `webcam_predict(model_name, camera_index)`: Cattura un'immagine dalla webcam e fa predizione con modello custom

### Formato Dati

I dati CSV devono avere il seguente formato:

```
timestamp,pir,touch_right,touch_left,light_right,light_left,ir_right,ir_left,label
```

### Requisiti

**Per Visione Artificiale (webcam + modello custom):**
- opencv-python >= 4.5.0
- keras >= 2.8.0  
- numpy >= 1.20.0

**Per ML su Sensori (opzionale):**
- scikit-learn >= 1.0.0
- pandas >= 1.3.0

### Classi Supportate (Modello Custom)

Il modello custom supporta le seguenti classi:
- aqualy
- calcolatrice_casio
- bicchiere
- iphone13
- mouse_wireless
- pennarello_giotto
- persona
- webcam_box

## Versione

v0.2.0 - Aggiunta dei blocchi per visione artificiale con webcam e predizione su immagini con modelli custom TensorFlow

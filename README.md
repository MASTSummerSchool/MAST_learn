# Machine Learning library for the MAST summer school

## How to install

Download and install [Mind+ Desktop app](https://mindplus.dfrobot.com).

Input the project URL: **<https://github.com/lozingaro/MAST_learn>** in the interface to import this library.

## Proposta Attività Didattiche Hands-On per la Scuola Estiva su IoT e AI

### Hands-On 1: Introduzione al Machine Learning

Insegnare agli studenti le basi del machine learning, con una spiegazione dei diversi tipi di apprendimento automatico e un focus sull'apprendimento supervisionato tramite attività di laboratorio.

1. **Introduzione al Machine Learning**:
   - Spiegazione dei diversi tipi di apprendimento automatico: supervisionato, non supervisionato e di rinforzo.
   - Focus sull'apprendimento supervisionato con esempi pratici.
   - Metriche di valutazione dei modelli di machine learning: accuratezza, precisione, recall.

2. **Attività di Laboratorio**:
   - **Raccolta Dati con Bittle**: Dotare Bittle di vari sensori (es. luce, movimento, tocco) e definire un insieme di condizioni ambientali (es. diversi livelli di luce, tipi di superfici).
   - **Etichettatura dei Dati**:
     - Spiegazione del concetto di etichettatura dei dati: etichettare i dati significa assegnare una "etichetta" o "label" ai dati raccolti, indicando la condizione o il risultato osservato.
     - Esempio concreto: posizionare Bittle in una stanza con luce moderata (condizione ambientale) e farlo camminare. I dati dei sensori raccolti durante questo movimento (ad esempio, la lettura dei sensori di movimento e luce) saranno etichettati come "camminata".
   - **Creazione di un Dataset**:
     - Utilizzare il modulo implementato in [MAST_sensor](https://github.com/AmedeoBonatti/MAST_sensor) per esaminare i risultati.
     - Organizzare i dati raccolti in formato tabellare con variabili indipendenti (letture dei sensori) e variabile dipendente (etichette dei movimenti).

Gli studenti comprenderanno le basi del machine learning e come raccogliere e etichettare i dati per creare un dataset per l'apprendimento supervisionato.

### Hands-On 2: Alberi Decisionali

Insegnare agli studenti come funzionano gli alberi decisionali e come implementarli per i compiti di classificazione attraverso un'attività unplugged e di laboratorio.

1. **Introduzione agli Alberi Decisionali**:
   - **Attività Unplugged**: Spiegare il concetto di alberi decisionali attraverso un'attività unplugged, utilizzando il riferimento [AI Unplugged](https://www.aiunplugged.org/english.pdf).

2. **Attività di Laboratorio**:
   - **Divisione del Dataset**: Dividere il dataset dell'Hands-On 1 in set di addestramento e test.
   - **Addestramento del Modello di Albero Decisionale**: Addestrare il modello di albero decisionale con i dati di addestramento usando il modulo `train_decision_tree`  implementato in [MAST_learn](https://github.com/lozingaro/MAST_learn).
   - **Validazione del Modello**: Validare il modello raccogliendo informazioni sul dataset di test.

Gli studenti impareranno come costruire, addestrare e valutare un modello di albero decisionale, fondendo le conoscenze acquisite durante l'attività unplugged con i risultati dell'Hands-On 1.

### Hands-On 3: Reti Neurali

Introdurre agli studenti le reti neurali e la loro applicazione in compiti di classificazione più complessi.

1. **Introduzione alle Reti Neurali**:
   - Spiegare le basi delle reti neurali, inclusi neuroni, strati e funzioni di attivazione.
   - Discutere come le reti neurali possono apprendere pattern complessi dai dati.

2. **Attività di Laboratorio**:
   - **Divisione del Dataset**: Dividere il dataset dell'Hands-On 1 in set di addestramento e test.
   - **Addestramento del Modello di Rete Neurale**: Addestrare il modello di rete neurale con i dati di addestramento usando il modulo `train_neural_network` implementato in [MAST_learn](https://github.com/lozingaro/MAST_learn).
   - **Validazione del Modello**: Validare il modello raccogliendo informazioni sul dataset di test.

3. **(optional) Sperimentazione**:
   - Permettere agli studenti di modificare l'architettura della rete neurale (es. numero di strati, neuroni) e osservare l'impatto sulle prestazioni.
   - Discutere il concetto di overfitting e come prevenirlo.

Gli studenti comprenderanno le basi delle reti neurali e come implementarle e sperimentare con esse per la classificazione dei movimenti di Bittle.

### Hands-On 4: Classificazione in Tempo Reale con Bittle (Progetto Finale)

Applicare i modelli addestrati per classificare i movimenti di Bittle in tempo reale.

1. **Distribuzione del Modello**:
   - Scegliere uno dei modelli addestrati (albero decisionale o rete neurale).

2. **Raccolta Dati in Tempo Reale**:
   - Raccogliere nuove informazioni dai sensori con il modulo `read_sensor` di [MAST_sensor](https://github.com/AmedeoBonatti/MAST_sensor).

3. **Classificazione in Tempo Reale**:
   - Ottenere la predizione a partire dai sensori con il blocco `infer` di [MAST_learn](https://github.com/lozingaro/MAST_learn).
   - Mostrare i risultati della classificazione su uno schermo o attraverso un dispositivo connesso.

4. **Feedback e Regolazioni**:
   - Permettere agli studenti di osservare la classificazione in tempo reale e fornire feedback.
   - Fare regolazioni per migliorare le prestazioni del modello se necessario.

Gli studenti sperimenteranno l'applicazione pratica dei loro modelli di machine learning, vedendo come possono essere utilizzati per classificare i movimenti in tempo reale.

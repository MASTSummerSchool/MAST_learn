from PetoiRobot import *

import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier


def train_decision_tree(filename: str, target: str) -> DecisionTreeClassifier:
    """
    Train a decision tree model on the data at the given path.

    Parameters:
    filename (str): The file path to the CSV data.
    target (str): The name of the target column in the data.

    Returns:
    DecisionTreeClassifier: The trained decision tree model.
    """
    # Controllo sui parametri
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")
    if not isinstance(target, str):
        raise ValueError("Il parametro 'target' deve essere una stringa.")

    print(f"Nome del file: {filename}")
    print(f"Colonna target: {target}")

    # Carica i dati
    # Il path deve essere composto dalla cartella sensor data nella home dell'utente (dipende dal sistema operativo) e il nome del file
    HOME = os.path.expanduser("~")
    path = f"{HOME}/sensor_data/{filename}"
    print(f"Path del file: {path}")
    data = pd.read_csv(path)
    print("Dati caricati con successo.")

    # Controllo se il target esiste nei dati
    if target not in data.columns:
        raise ValueError(f"La colonna target '{target}' non esiste nei dati.")
    print(f"Colonna target '{target}' trovata nei dati.")

    # Dividi i dati in caratteristiche (features) e target
    X = data.drop(target, axis=1)
    y = data[target]
    print("Dati divisi in caratteristiche (features) e target.")

    # Addestramento del modello ad albero decisionale
    model = DecisionTreeClassifier()
    model.fit(X, y)
    print("Modello ad albero decisionale addestrato con successo.")

    return model


def train_neural_network(filename: str, target: str, hidden_layer_sizes=(100,), max_iter=200) -> MLPClassifier:
    """
    Train a neural network model on the data at the given path using MLPClassifier.

    Parameters:
    filename (str): The file path to the CSV data.
    target (str): The name of the target column in the data.
    hidden_layer_sizes (tuple): The ith element represents the number of neurons in the ith hidden layer.
    max_iter (int): Maximum number of iterations.

    Returns:
    MLPClassifier: The trained neural network model.
    """
    # Controllo sui parametri
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")
    if not isinstance(target, str):
        raise ValueError("Il parametro 'target' deve essere una stringa.")
    if not isinstance(hidden_layer_sizes, tuple):
        raise ValueError(
            "Il parametro 'hidden_layer_sizes' deve essere una tupla.")
    if not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError(
            "Il parametro 'max_iter' deve essere un intero positivo.")

    print(f"Nome del file: {filename}")
    print(f"Colonna target: {target}")
    print(f"Dimensioni dei layer nascosti: {hidden_layer_sizes}")
    print(f"Numero massimo di iterazioni: {max_iter}")

    # Carica i dati
    # Il path deve essere composto dalla cartella sensor data nella home dell'utente (dipende dal sistema operativo) e il nome del file
    HOME = os.path.expanduser("~")
    path = f"{HOME}/sensor_data/{filename}"
    print(f"Path del file: {path}")
    data = pd.read_csv(path)
    print("Dati caricati con successo.")

    # Controllo se il target esiste nei dati
    if target not in data.columns:
        raise ValueError(f"La colonna target '{target}' non esiste nei dati.")
    print(f"Colonna target '{target}' trovata nei dati.")

    # Dividi i dati in caratteristiche (features) e target
    X = data.drop(target, axis=1)
    y = data[target]
    print("Dati divisi in caratteristiche (features) e target.")

    # Addestramento del modello di rete neurale
    model = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter)
    model.fit(X, y)
    print("Modello di rete neurale addestrato con successo.")

    return model


def infer(model, data: list) -> str:
    """
    Make predictions using the trained model on the given data.

    Parameters:
    model: The trained model to use for prediction.
    data (list): The data to make predictions on.

    Returns:
    str: The predicted class label.
    """

    # Controllo sui parametri
    if not isinstance(data, list):
        raise ValueError("Il parametro 'data' deve essere una lista.")

    # Predizione
    prediction = model.predict([data])[0]
    print(f"Predizione effettuata: {prediction}")

    return prediction

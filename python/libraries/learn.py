from sklearn import tree, neural_network

from typing import List, Tuple
from PetoiRobot import *

from datetime import datetime

import os
import platform
import collections

import pandas as pd


def compose_path(filename: str, file_ext: str = '.csv') -> str:
    """
    Compose the path to the CSV data file.

    Parameters:
    filename (str): The name of the file.

    Returns:
    str: The path to the file.
    """
    # Controllo sui parametri
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")

    # Il path deve essere composto dalla cartella sensor data nella home dell'utente (dipende dal sistema operativo) e il nome del file
    # Check if we are on windows, mac or linux:
    if platform.system() == "Windows":
        sep = '\\'
        home_dir = os.getenv('HOMEDRIVE')
        home_path = os.getenv('HomePath')
        config_dir = home_dir + home_path
    else:  # for Linux & macOS
        sep = '/'
        home = os.getenv('HOME')
        config_dir = home

    # Create the data directory:
    data_dir = config_dir + sep + 'sensor_data'

    # Check if it exists:
    if not os.path.exists(data_dir):

        # Create the directory if it does not exist
        os.makedirs(data_dir)

    # Check if the file name already exists and if yes make it unique:
    file_dir = data_dir + sep + filename + file_ext

    return file_dir


def load_data_pd(path: str) -> Tuple[List[str], List[List[str]]]:
    """
    Load the data from the CSV file at the given path.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    Tuple[List[str], List[List[str]]]: The data in the CSV file.
    """
    # Controllo sui parametri
    if not isinstance(path, str):
        raise ValueError("Il parametro 'path' deve essere una stringa.")

    # Carica i dati con pandas
    data = pd.read_csv(path)

    return data


def datetime_to_seconds(dt_str: str) -> int:
    """
    Convert the given datetime string to seconds.

    Parameters:
    dt_str (str): The datetime string.

    Returns:
    int: The number of seconds.
    """
    # Controllo sui parametri
    if not isinstance(dt_str, str):
        raise ValueError("Il parametro 'dt_str' deve essere una stringa.")

    # Converte in datetime from string to seconds
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')
    return int(dt.timestamp())


def preprocess_data(data):
    # Controllo sui parametri
    if not isinstance(data, list):
        raise ValueError("Il parametro 'data' deve essere una lista.")

    # Preprocessamento dei dati
    X = []
    y = []
    for row in data:
        X_tmp = []
        # create a list of features and append to X
        # timestamp: datetime to int seconds the first value
        if isinstance(row[0], str):
            date = row[0]
        else:
            date = row[0].strftime('%Y-%m-%d %H:%M:%S.%f')
        seconds = datetime_to_seconds(date)
        X_tmp.append(float(seconds))  # Convert to float
        # pir,touch_left,touch_right,light_left,light_right,ir_left,ir_right: int values
        for j in range(1, 8):
            X_tmp.append(float(row[j]))  # Convert to float
        X.append(X_tmp)
        # label: append to y
        y.append(row[8].replace("\"", ""))
    return X, y


def preprocess_data_pd(data):
    """
    Preprocess the data.

    Parameters:
    data: The data to preprocess.
    """
    # Controllo sui parametri
    if not isinstance(data, pd.DataFrame):
        raise ValueError(
            "Il parametro 'data' deve essere un DataFrame di pandas.")

    # Split the data into features and labels
    X = data.drop('label', axis=1)
    y = data['label']

    # Convert the timestamp to seconds
    X['timestamp'] = pd.to_datetime(X['timestamp'])
    X['timestamp'] = X['timestamp'].astype(int)

    # Drop columns that contains only null values (-1)
    X = X.loc[:, (X != -1).any(axis=0)]

    # Convert numerical values to float
    X = X.astype(float)

    return X, y


def train_decision_tree(filename: str):
    """
    Train a decision tree model on the data at the given path.

    Parameters:
    filename (str): The file path to the CSV data.

    Returns:
    DecisionTreeClassifier: The trained decision tree model.
    """
    # Controllo sui parametri
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")
    print(f"Nome del file: {filename}")

    # Componi il path
    path = compose_path(filename)
    print(f"Path del file: {path}")

    # Carica i dati
    data = load_data_pd(path)
    print("Dati caricati con successo.")

    # Preprocessamento dei dati
    X, y = preprocess_data_pd(data)
    print("Dati convertiti.")
    # print(X)

    # Addestramento del modello di albero decisionale
    model = tree.DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    print("Modello di albero decisionale addestrato con successo.")

    return model


def train_neural_network(filename: str, hidden_layer_sizes=(100,), max_iter=200):
    """
    Train a neural network model on the data at the given path using MLPClassifier.

    Parameters:
    filename (str): The file path to the CSV data.
    hidden_layer_sizes (tuple): The ith element represents the number of neurons in the ith hidden layer.
    max_iter (int): Maximum number of iterations.

    Returns:
    MLPClassifier: The trained neural network model.
    """
    # Controllo sui parametri
    if not isinstance(filename, str):
        raise ValueError("Il parametro 'filename' deve essere una stringa.")
    if not isinstance(hidden_layer_sizes, tuple):
        raise ValueError(
            "Il parametro 'hidden_layer_sizes' deve essere una tupla.")
    if not isinstance(max_iter, int):
        raise ValueError("Il parametro 'max_iter' deve essere un intero.")
    print(f"Nome del file: {filename}")

    # Componi il path
    path = compose_path(filename)
    print(f"Path del file: {path}")

    # Carica i dati
    data = load_data_pd(path)
    print("Dati caricati con successo.")

    # Pre-processa i dati
    X, y = preprocess_data_pd(data)
    print("Dati convertiti.")
    # print(X)

    # Addestramento del modello di rete neurale
    model = neural_network.MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter, random_state=42)
    model.fit(X, y)
    print("Modello di rete neurale addestrato con successo.")

    return model


def infer(model, data: list) -> list:
    """
    Make predictions using the trained model on the given data.

    Parameters:
    model: The trained model to use for prediction.
    data (list): The data to make predictions on.

    Returns:
    list: The list of predicted class label.
    """
    # Controllo sui parametri
    if not isinstance(data, list):
        raise ValueError("Il parametro 'data' deve essere una lista.")
        if not isinstance(data[0], dict):
            raise ValueError(
                "Il primo valore di 'data' deve essere un dizionario.")

    # Creazione del DataFrame di pandas
    data = pd.DataFrame(data)

    # Preprocessamento dei dati
    X, _ = preprocess_data_pd(data)
    
    # Predizione
    labels = model.predict(X)

    # Ritorna la label più comune
    label = collections.Counter(labels).most_common(1)[0][0]
    print(f"Label: {label}")

    return label


def main():
    # Addestramento del modello di rete neurale
    # model = train_decision_tree("test")
    model = train_neural_network("test")
    label = infer(model, [{
        'timestamp': '2021-06-01 17:10:01.3449',
        'pir': 1,
        'touch_right': -1,
        'touch_left': -1,
        'light_right': -1,
        'light_left': -1,
        'ir_right': -1,
        'ir_left': -1,
        'label': 'aula 8'
    }])
    print(label)


if __name__ == "__main__":
    main()

import sklearn
import pandas as pd


def train_decision_tree(path, target):
    # Load the data
    data = pd.read_csv(path)

    # Split the data into features and target
    X = data.drop(target, axis=1)
    y = data[target]

    # Train a decision tree model
    model = sklearn.tree.DecisionTreeClassifier()
    model.fit(X, y)

    return model


def train_neural_network(path, target):
    # Load the data
    data = pd.read_csv(path)

    # Split the data into features and target
    X = data.drop(target, axis=1)
    y = data[target]

    # Train a neural network model
    model = sklearn.neural_network.MLPClassifier()
    model.fit(X, y)

    return model


def infer(model, data):
    # Make predictions using the model
    predictions = model.predict(data)

    # prediction is a single label
    if len(predictions.shape) == 1:
        predictions = pd.DataFrame(predictions, columns=['prediction'])
    else:
        predictions = pd.DataFrame(predictions, columns=[
                                   'prediction_{}'.format(i) for i in range(predictions.shape[1])])

    return predictions

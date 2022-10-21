""""
Inititialize a model from the datasets then evaluates how it performs against unknow datasets.
"""
import sys
import numpy
from models.mock import Mock

def train(model, training_dataset):
    """Train the provided model using the training_dataset
        model_class : a class inheriting from class models.Model
        training_dataset : a pandas dataframe with the training data
    """
    model.initialize_from(training_dataset)

def evaluate_timeserie(model, timeserie):
    return model.evaluate_timeserie(timeserie)

def score_timeserie(prediction, observation):
    return numpy.sqrt(numpy.square(prediction["Ti"] - observation["Ti"])).sum()
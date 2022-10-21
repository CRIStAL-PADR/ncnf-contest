import sys
import unittest
from models.model import Model
from models.mock import Mock
from contest.evaluate import *
import pandas

class TestModel(unittest.TestCase):
    model_class = Mock 

    def test_model(self):
        self.assertNotEqual(self.model_class.name, "Undefined")
        self.assertNotEqual(self.model_class.description, "Undefined")
        self.assertNotEqual(self.model_class.authors, "Undefined")

    def test_inheritance(self):
        model = self.model_class()
        self.assertTrue(isinstance(model, Model))

    def test_initialize_from(self):
        model = self.model_class()
        model.initialize_from(pandas.read_csv("datasets/dataset-1.csv"))

    def test_evaluate(self):
        model = self.model_class()
        model.initialize_from(pandas.read_csv("datasets/dataset-1.csv"))
        self.assertTrue(model.evaluate({"Ta" : 0.0}), float)

    def test_evaluate_timeserie(self):
        timeserie=pandas.read_csv("datasets/dataset-1.csv")
        model = train(self.model_class, timeserie)
        model = self.model_class()
        model.initialize_from(pandas.read_csv("datasets/dataset-1.csv"))

        self.assertTrue(isinstance(model.evaluate_timeserie(timeserie), list))
        self.assertEqual(len(timeserie), len(model.evaluate_timeserie(timeserie)))

if __name__ == '__main__':
    unittest.main()
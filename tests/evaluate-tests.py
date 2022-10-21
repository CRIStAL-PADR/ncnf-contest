import sys
import unittest
from models.model import Model
from models.mock import Mock
from contest.evaluate import *
import pandas

class TestEvaluate(unittest.TestCase):
    model_class = Mock 

    def test_train(self):
        model = self.model_class()
        train(model, pandas.read_csv("datasets/dataset-1.csv"))
        self.assertTrue(isinstance(model, self.model_class))

    def test_evaluate_timeserie(self):
        timeserie=pandas.read_csv("datasets/dataset-1.csv")
        model = self.model_class()
        train(model, timeserie)
        self.assertTrue(isinstance(evaluate_timeserie(model, timeserie), pandas.DataFrame))
        self.assertEqual(len(timeserie), len(model.evaluate_timeserie(timeserie)))

    def test_score_timeserie(self):
        timeserie=pandas.read_csv("datasets/dataset-1.csv")
        model = self.model_class()
        train(model, timeserie)
        tprediction = evaluate_timeserie(model, timeserie)
        tscore = score_timeserie(tprediction, timeserie)
        self.assertEquals(tscore, 0)


if __name__ == '__main__':
    unittest.main()
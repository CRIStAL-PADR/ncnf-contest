import random
from models.model import Model

class Mock(Model):
    name = "Copy the temperature value from the input data"
    description = """A not working thermal model"""
    authors = "Damien Marchal"
    variables = {
        "Ti:" : { "desc" : "Internal temperature" },
        "Ta:" : { "desc" : "Ambient temperature" }
    }

    def __init__(self, *args, **kwargs):
        pass

    def do_initialization_from(self, dataset): 
        pass 

    def do_evaluate(self, inputs_variables):
        return inputs_variables["Ti"]

    def do_evaluate_timeserie(self, timeserie):
        results = []
        for index, row in timeserie.iterrows(): 
            results.append(
                {
                    "Date" : row["Date"],
                    "Ti"   : self.evaluate(row) 
                }
            )
        return results
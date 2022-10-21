import pandas

class Model(object):
    name = "Undefined"
    description = "Undefined"
    authors = "Undefined"
    
    def initialize_from(self, dataset):
        self.do_initialization_from(dataset) 
        return True        

    def evaluate(self, inputs_variables):
        return self.do_evaluate(inputs_variables)

    def evaluate_timeserie(self, timeserie):
        r = self.do_evaluate_timeserie(timeserie)
        return pandas.DataFrame.from_records(r)



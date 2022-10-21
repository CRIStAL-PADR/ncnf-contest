from ctypes import alignment
import pandas
import json
import os
from evaluate import evaluate_timeserie, train, score_timeserie
from models.mock import Mock
from datetime import datetime

model_classes = [Mock]
building_datasets = ["datasets/dataset-1.csv"]

all_runs = []
for model_class in model_classes:
    print("Evaluating: ", model_class.name)

    for building_dataset in building_datasets:
        path, filename = os.path.split(building_dataset)
        print("Datatype: " , building_dataset)
        model = model_class()
        timeserie = pandas.read_csv(building_dataset)

        a = datetime.now()       
        train(model, timeserie)
        training_time = datetime.now() - a
        a = datetime.now()
        prediction = evaluate_timeserie(model, timeserie)
        evaluation_time = datetime.now() - a
        
        score = score_timeserie(prediction, timeserie)

        result = {
            "model" : model_class.name,
            "dataset" : building_dataset,
            "training-time" : training_time.total_seconds(),  
            "evaluation-time" : evaluation_time.total_seconds(),
            "score" : score
        }
        all_runs.append(result)

        result["prediction"] : prediction.to_dict(orient="records")

        outfile = "results/"+model_class.name+"-"+filename+".json"
        with open(outfile, "w") as file:
            file.write(json.dumps(result))
        print("Execution saved into: ", outfile)
    
    print("Time: ", all_runs)     
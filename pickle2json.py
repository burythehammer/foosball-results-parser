import json as JSON
import pickle
import jsonpickle

INPUT_FILE_PATH = "foosdb.pickle"
OUTPUT_FILE_PATH = "foosdb.json"

def read_results(input_path):
    f = open(input_path, 'rw')
    return pickle.loads(f.read())

def write_results(results, output_path):
    serialized = jsonpickle.encode(results)

    f = open(output_path, 'w')
    f.write(serialized)

results = read_results(INPUT_FILE_PATH)
write_results(results, OUTPUT_FILE_PATH)

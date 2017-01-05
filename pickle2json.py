import pickle
import jsonpickle
import json as JSON

INPUT_FILE_PATH = "foosdb.pickle"
OUTPUT_FILE_PATH = "foosdb.json"

def read_results(input_path):
    pickle_file = open(input_path, 'r')
    something = pickle_file.read
    print type(something)
    return pickle.loads(pickle_file.read())

def write_results_to_json(results, output_path):
    serialized = jsonpickle.encode(results)
    json_file = open(output_path, 'w')
    json_file.write(serialized)

def pickle2json():
    results = read_results(INPUT_FILE_PATH)
    write_results_to_json(results, OUTPUT_FILE_PATH)


def json2python():
    output_file = open(OUTPUT_FILE_PATH, 'r')
    results = JSON.loads(output_file.read)
    print results 


pickle2json()
json2python()

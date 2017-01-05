import pickle
import jsonpickle
import json as JSON
from core import FoosballMatch

INPUT_FILE_PATH = "foosdb.pickle"
OUTPUT_FILE_PATH = "foosdb.json"

def read_results(input_path):
    pickle_file = open(input_path, 'r')
    return pickle.loads(pickle_file.read())

def write_results_to_json(results, output_path):
    serialized = jsonpickle.encode(results)
    json_file = open(output_path, 'w')
    json_file.write(serialized)

def transform_results(results):

    new_matches = []

    for key, value in results.items():
        for result_id, m in value.items():
            match = FoosballMatch(result_id, m.players1, m.players2, m.score1, m.score2, m.when)
            new_matches.append(match)

    return new_matches

def pickle2json():
    results = read_results(INPUT_FILE_PATH)
    new_results = transform_results(results)
    write_results_to_json(new_results, OUTPUT_FILE_PATH)




pickle2json()
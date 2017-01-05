"""Searches entire JSON and lists unique players"""

import json as JSON

INPUT_FILE_PATH = "foosdb.json"

def read_results(input_path):
    """Reads results from json file"""

    json_file = open(input_path, 'r')
    return JSON.loads(json_file.read())

def get_players(results):
    """Returns set of players from raw json"""

    players = set()
    for result in results:
        for player in result['players1']:
            players.add(player)

        for player in result['players2']:
            players.add(player)

    return players

def main():
    """Default method"""
    results = read_results(INPUT_FILE_PATH)
    players = get_players(results)
    print players

main()

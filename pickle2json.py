"""A simple converter to turn a pickle dump of Foosball results into json format"""
import pickle
import jsonpickle
from core import FoosballMatch

INPUT_FILE_PATH = "foosdb.pickle"
OUTPUT_FILE_PATH = "foosdb.json"

PLAYER_MAP = {
    'U0HTRQ5HQ': "rafal.gancarz",
    'U0HTPM4P8': "matt.long",
    'U1CUW4Z7S': "benv",
    'U1NGZQV3M': "alla.babkina",
    'U0JNVCVRT': "eeichinger",
    'U0HTQ6XQQ': "davibo",
    'U0KCZ16LT': "cameron",
    'U0HTSHTR9': "sam-e",
    'U0J8LB74P': "lorenzo",
    'U07V0F5AS': "jeanmarie.ferdegue",
    'U0J8ETRH7': "antonio",
    'U0HTPS3JS': "tristan",
    'U0HTJ2DK6': "norbert.annus",
    'U0HTVEJKC': "carloslindo",
    'U17V6C5K6': "pegerto",
    'U0HTVTLBS': "brett.mack",
    'U0834SYHL': "nicki.watt",
    'U0HTR4KRT': "steve",
    'U0JBNHJ3X': "maartens",
    'U0HTPUK8R': "andrew.morgan",
    'U0W5T83EK': "enekofb",
    'U0KA76231': "henry.barnett",
    'U16DF5LQH': "benji",
    'U2SDVEFL0': "tommy.situ",
    'U0HTQJMHN': "fahran",
    'U21CBD6KX': "paul.prendergast",
    'U0UEK3GMR': "tom.cunliffe",
    'U0J13UGAF': "tareq",
    'U0J0XLJUD': "mateus.pimenta.oc",
    'U0JB5HB46': "domfox"
}

def read_results(input_path):
    """Reads foosball results from the pickle file"""
    pickle_file = open(input_path, 'r')
    return pickle.loads(pickle_file.read())

def write_results(results, output_path):
    """Writes foosball results to JSON file"""
    serialized = jsonpickle.encode(results)
    json_file = open(output_path, 'w')
    json_file.write(serialized)

def transform_results(results):
    """Transforms results from old format to new format"""
    new_matches = []

    for match_id, match in results['matches'].items():
        team1 = transform_names_in_team(match.players1)
        team2 = transform_names_in_team(match.players2)

        match = FoosballMatch(match_id, team1, team2, match.score1, match.score2, match.when)
        new_matches.append(match)

    return new_matches

def transform_names_in_team(team):
    """Converts player names in team from unique slack id to slack name"""
    new_team = []
    for player in team:
        new_team.append(PLAYER_MAP[player])
    return new_team

def main():
    """Main method"""

    results = read_results(INPUT_FILE_PATH)
    new_results = transform_results(results)
    write_results(new_results, OUTPUT_FILE_PATH)


main()

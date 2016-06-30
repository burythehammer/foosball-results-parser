import dateutil.parser
import jsonpickle

from FoosballResult import FoosballResult

INPUT_FILE_PATH = "raw_results.txt"
OUTPUT_FILE_PATH = "output.json"


def parse_date(input_date):
    input_date.strip('-').strip()
    return dateutil.parser.parse(input_date)


def get_result_map(symbols):
    print symbols
    result = {
        'reporter': '@' + symbols[0],
        'time': symbols[1],
        'team1': (symbols[4], symbols[5]),
        'team2': (symbols[7], symbols[8]),
        'score': symbols[9]
    }
    return result


def construct_timestamp(time, current_date):
    datetime_string = time + " " + current_date.strftime("%B %d, %Y")
    return dateutil.parser.parse(datetime_string)


def parse_result(line, current_date):
    symbols = filter(None, line.replace('\n', ' ').translate(None, '[]').split(' '))

    result_map = get_result_map(symbols)

    timestamp = construct_timestamp(result_map['time'], current_date)
    result = FoosballResult(result_map['reporter'], timestamp, result_map['team1'], result_map['team2'],
                            result_map['score'])

    return result


def get_results_from_file(file_path):
    results_file = open(file_path, 'r')
    current_date = None
    results_list = []

    for line in results_file:
        if line.strip():
            if '-----' in line:
                current_date = parse_date(line)
            else:
                result = parse_result(line + next(results_file), current_date)
                results_list.append(result)

    return results_list


results = get_results_from_file(INPUT_FILE_PATH)
serialized = jsonpickle.encode(results)

f = open(OUTPUT_FILE_PATH, 'w')
f.write(serialized)

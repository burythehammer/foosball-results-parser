import dateutil.parser

from FoosballResult import FoosballResult

INPUT_FILE_PATH = "results.txt"


def parse_date(input):
    input.strip('-').strip()
    return dateutil.parser.parse(input)


def get_result_map(symbols):
    result = {'reporter': '@' + symbols[0], 'time': symbols[1] + symbols[2],
              'team1': (symbols[5], symbols[6]), 'team2': (symbols[8], symbols[9]), 'score': symbols[10]}

    return result


def construct_timestamp(param, current_date):
    pass


def parse_result(line, current_date):
    symbols = filter(None, line.replace('\n', ' ').translate(None, '[]').split(' '))

    result_map = get_result_map(symbols)
    print result_map

    timestamp = construct_timestamp(result_map['time'], current_date)
    result = FoosballResult(result_map['reporter'], timestamp, result_map['team1'], result_map['team2'], result_map['score'])

    return result


def get_results_from_file():
    results_file = open(INPUT_FILE_PATH, 'r')
    current_date = None

    for line in results_file:
        if line.strip():
            if '-----' in line:
                current_date = parse_date(line)
            else:
                parse_result(line + next(results_file), current_date)
                pass


get_results_from_file()

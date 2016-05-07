class FoosballResult:

    def __init__(self, reporter, timestamp, team1, team2, score):
        self.reporter = reporter
        self.timestamp = timestamp
        self.team1 = team1
        self.team2 = team2

        scores = score.split('-')

        self.team1score = scores[0]
        self.team2score = scores[1]

class Result():
    def __init__(self, reporter, timestamp, team1, team2, score1, score2):
        self.reporter = reporter
        self.timestamp = timestamp.isoformat()
        self.team1 = team1
        self.team2 = team2
        self.team1score = score1
        self.team2score = score2

class Match():
    def __init__(self, players1, players2, score1, score2, when):

        self.players1 = players1
        self.players2 = players2
        self.score1 = score1
        self.score2 = score2
        self.when = when


class FoosballMatch():
    def __init__(self, match_id, players1, players2, score1, score2, timestamp):
        self.match_id = match_id
        self.players1 = players1
        self.players2 = players2
        self.score1 = score1
        self.score2 = score2
        self.timestamp = timestamp.isoformat()

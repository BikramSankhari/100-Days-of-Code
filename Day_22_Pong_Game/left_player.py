from plate import Plate
from score_board import ScoreBoard


class LeftPlayer:
    def __init__(self):
        self.plate = Plate(-380)
        self.score_board = ScoreBoard((-70, 200))


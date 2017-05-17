from MyConstants import Directions

class Motor():
    def __init__(self, side):
        self.Speed = -1
        self.Direction = Directions.Stand
        self.Side = side
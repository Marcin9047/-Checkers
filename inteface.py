

class Board:
    def __init__(self, size, players):
        self.size = size
        self.players = players

    def draw():
        pass


class Space:
    def __init__(self, size, pos, color):
        self.size = size
        self.pos = pos
        self.color = color

    def draw():
        pass


class Pawn:
    def __init__(self, owner, pos):
        self.owner = owner
        self.pos = pos
        self.isactive = True
        self.isqueen = False

    def draw():
        pass

    def move():
        pass

    def is_able_to_capture():
        return False

    def capture():
        pass


class Player:
    def __init__(self, pawns):
        self.act_pawns = pawns

    def is_active():
        return True

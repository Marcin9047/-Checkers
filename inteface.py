import pygame
from pygame.locals import Rect

black = (0, 0, 0)
white = (255, 255, 255)


class Board:
    def __init__(self, game, size, players):
        self.size = size
        self.game = game
        self.players = players
        pawns = []
        for ind in range(2):
            for i in range(4):
                for y in range(3):
                    cord = (500 + 55 + 220 * i + 110 * ((y - ind) % 2), 50 + 55 + (ind * 550) + (110 * y))

                    if y + (5 * ind) % 2 == 0:
                        pos_x = 1 + (2 * i)
                    else:
                        pos_x = 2 + (2 * i)

                    pos_y = 1 + y + (ind * 5)
                    pos = [pos_x, pos_y]
                    pawn = Pawn(self.game.board_bgr, self.game, self.players[ind], pos, cord)
                    pawns.append(pawn)
            self.players[ind].set_pawns(pawns)



    def draw_num(self):
        for num in range(2):
            for i in range(8):
                font = pygame.font.Font(None, 25)
                text = font.render(f'{i + 1}', 1, black)
                textpos = text.get_rect()
                if num == 0:
                    textpos = textpos.move(480, 105 + (110 * i))
                else:
                    textpos = textpos.move(550 + (110 * i), 950)
                self.game.board_bgr.blit(text, textpos)


    def draw(self):
        surf = self.game.board_bgr
        #110 per squere
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    color = white
                else:
                    color = black
                space = Space(surf, 110, (500 + 110 * x, 50 + 110 * y), color)
                space.draw()
        pygame.draw.rect(surf, black, Rect(500, 50, 880, 880), 5)
        self.draw_num()

        for pawn in self.players[1].get_pawns():
            if pawn.pos == [2, 6]:
                pawn.move([1, 5])


        for player in self.players:
            for i in player.get_pawns():
                i.draw()
        self.game.screen.blit(surf, (0, 0))
        pygame.display.flip()


class Space:
    def __init__(self, surf, size, pos, color):
        self.surf = surf
        self.size = size
        self.pos = pos
        self.color = color

    def draw(self):
        rect = Rect(self.pos[0], self.pos[1], 110, 110)
        pygame.draw.rect(self.surf, self.color, rect, 0, 2)


class Pawn:
    def __init__(self, surf, game, owner, pos, cord):
        self.owner = owner
        self.pos = pos
        self.cords = cord
        self.isactive = True
        self.isqueen = False
        self.surf = surf
        self.game = game

    def draw(self):
        pygame.draw.circle(self.surf, self.owner.color, self.cords, 40)
        pygame.draw.circle(self.surf, black, self.cords, 40, 2)

    def move(self, pos):
        for player in self.game.players:
            for pawn in player.get_pawns():
                if pawn.pos == pos:
                    return 0
        self.set_cords(pos)
        self.pos = pos

    def set_cords(self, new_pos):
        x, y = self.cords
        if new_pos[0] > self.pos[0]:
            x_cord = self.cords[0] + 110
        else:
            x_cord = self.cords[0] - 110
        if new_pos[1] > self.pos[1]:
            y_cord = self.cords[1] + 110
        else:
            y_cord = self.cords[1] - 110

        self.cords = [x_cord, y_cord]


    def is_able_to_capture():
        return False

    def capture():
        pass


class Player:
    def __init__(self, name, color):
        self.name = name
        self.pawns = []
        self.color = color

    def set_pawns(self, pawns):
        self.pawns = pawns

    def get_pawns(self):
        return self.pawns

    def is_active():
        return True


class Game:
    def __init__(self, size, players):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Checkers ')
        self.board_bgr = pygame.Surface(self.screen.get_size())
        self.board_bgr = self.board_bgr.convert()
        self.board_bgr.fill((255, 255, 255))
        self.players = []
        colors = ((94, 74, 54), (139, 121, 102))
        for num, player in enumerate(players):
            new = Player(player, colors[num - 1])
            self.players.append(new)
        self.board = Board(self, size, self.players)

    def run(self):
        while True:
            pygame.init()
            self.screen.blit(self.board_bgr, (0, 0))
            pygame.display.flip()
            self.board.draw()
            self.do_action()

    def do_action(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # if event.type == pygame.MOUSEBUTTONUP:
                #     paused = False
        pygame.display.flip()


game = Game(34, ("Marcin", "Dawid"))
game.run()

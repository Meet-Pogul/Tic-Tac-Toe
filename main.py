import pygame
import os

FPS = 60
CLOCK = pygame.time.Clock()


def loop(func1):
    def nowexec(self, *args):
        while True:
            func1(self, *args)
            pygame.display.update()
            CLOCK.tick(FPS)
    return nowexec


class TicTacToe:
    def __init__(self):
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (190, 30, 30)

        # SCREEN SIZE
        self.SCREENWIDTH = 600
        self.SCREENHEIGHT = 700

        self.gridlines = [((0, 200), (600, 200)),
                          ((0, 400), (600, 400)),
                          ((200, 0), (200, 600)),
                          ((400, 0), (400, 600))]

        self.currentValue = 0

    def run(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '400,50'

        pygame.init()
        pygame.mixer.init()

        # Creating Window
        self.WINDOW = pygame.display.set_mode(
            (self.SCREENWIDTH, self.SCREENHEIGHT))

        pygame.display.set_caption("Tic Tac Toe")

        # Images
        self.wcimg = pygame.image.load(r"gallery\image\wc.jpg")
        self.wcimg = pygame.transform.scale(
            self.wcimg, (self.SCREENWIDTH, self.SCREENHEIGHT)).convert_alpha()

        self.ximg = pygame.image.load(r"gallery\image\x.png")
        self.oimg = pygame.image.load(r"gallery\image\o.png")
        self.icon = pygame.image.load(r"gallery\image\icon.png")
        self.icon = pygame.transform.scale(
            self.icon, (60, 60)).convert_alpha()

        pygame.display.set_icon(self.icon)

        self.welcome()

    @loop
    def welcome(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.startgame()
                    quit()
        self.MATRIX = [[0 for i in range(3)] for j in range(3)]
        self.currentValue = 0
        self.WINDOW.blit(self.wcimg, (0, 0))
        self.textScreen("Tic Tac Toe", self.RED,
                        145, self.SCREENHEIGHT/2 - 70, 90)
        self.textScreen("Enter to Start Game", self.RED,
                        5, self.SCREENHEIGHT/2, 90)

    @loop
    def startgame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.updateMatrix(pos)
                self.checkMatrix()

        self.WINDOW.blit(self.wcimg, (0, 0))
        self.blitMatrix()
        self.drawGrid()
        self.textScreen("Player "+self.currentPlayer().upper() +
                        "'s Turn", self.RED)

    def textScreen(self, text, color, x=50, y=615, fsize=100):
        """Show Text on Screen"""
        FONT = pygame.font.SysFont(None, fsize)
        screen_text = FONT.render(text, True, color)
        self.WINDOW.blit(screen_text, [int(x), int(y)])

    def drawGrid(self):
        for lines in self.gridlines:
            pygame.draw.line(self.WINDOW, self.WHITE,
                             lines[0], lines[1], 10)

        pygame.draw.rect(self.WINDOW, self.WHITE, (0, 600, 600, 100))

    def updateMatrix(self, pos):
        if self.MATRIX[pos[1]//200][pos[0]//200] == 0:
            self.MATRIX[pos[1]//200][pos[0]//200] = self.currentPlayer()
            self.currentValue += 1

    def currentPlayer(self):
        if self.currentValue % 2 == 0:
            ch = 'o'
        else:
            ch = 'x'
        return ch

    def blitMatrix(self):
        for i in range(3):
            for j in range(3):
                if self.MATRIX[i][j] == 'o':
                    self.WINDOW.blit(self.oimg, (j*200, i*200))
                elif self.MATRIX[i][j] == 'x':
                    self.WINDOW.blit(self.ximg, (j*200, i*200))

    def checkMatrix(self):
        if self.currentValue > 8:
            self.result(0, "Tie")
            return

        # Normal
        for i in self.MATRIX:
            if i[0] != 0:
                flag = 1
                for j in i[1:]:
                    if j != i[0]:
                        flag = 0
                        break
                if flag != 0:
                    self.result(i[0])

        # Transpose
        for i in zip(*self.MATRIX):
            if i[0] != 0:
                flag = 1
                for j in i[1:]:
                    if j != i[0]:
                        flag = 0
                        break

                if flag != 0:
                    self.result(i[0])

        # Diagonal
        flag = 1
        k = 1
        for i in self.MATRIX[1:]:
            if self.MATRIX[0][0] == 0 or self.MATRIX[0][0] != i[k]:
                flag = 0
                break
            k += 1
        if flag != 0:
            self.result(self.MATRIX[0][0])

        # Reverse Diagonal
        flag = 1
        k = 1
        for i in self.MATRIX[1:]:
            if self.MATRIX[0][2] == 0 or self.MATRIX[0][2] != i[k]:
                flag = 0
                break
            k -= 1
        if flag != 0:
            self.result(self.MATRIX[0][2])

    @loop
    def result(self, player, game="Won"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.welcome()
                    quit()
        self.WINDOW.blit(self.wcimg, (0, 0))
        self.blitMatrix()
        self.drawGrid()
        if game == "Won":
            self.textScreen("Player "+player.upper() + " " +
                            game, self.RED, 80)
        elif game == "Tie":
            self.textScreen("Game is " +
                            game, self.RED, 100)


if __name__ == "__main__":
    game = TicTacToe()
    game.run()

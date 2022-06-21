import pygame
import random
import sys
import warnings
from pygame.locals import *
import SpeechEngine
import Agent
import maze
import Button

random.seed(42)
warnings.filterwarnings('ignore')

pygame.init()
# fps config
fpsClock = pygame.time.Clock()
FPS = 30

WINDOWHEIGHT = 600
WINDOWWIDTH = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Mystery Maze')

# training set for alignment loader
train_set_x, train_set_y = SpeechEngine.prepare_tools()

# init the game
game = 1
ingame = False
gamemenu = False

# Load Images
Background1 = pygame.image.load('./img/resource/background1.png')
game1bg = pygame.image.load('./img/resource/game1.jpg')
game2bg = pygame.image.load('./img/resource/game2.jpg')
Background2 = pygame.image.load('./img/resource/background2.png')
Background1 = pygame.transform.scale(Background1, (WINDOWWIDTH, WINDOWHEIGHT))
Background2 = pygame.transform.scale(Background2, (WINDOWWIDTH, WINDOWHEIGHT))
game1bg = pygame.transform.scale(game1bg, (WINDOWWIDTH, WINDOWHEIGHT))
game2bg = pygame.transform.scale(game2bg, (WINDOWWIDTH, WINDOWHEIGHT))

# Load Buttons
font = pygame.font.SysFont("comicsans", 20)
button_center = Button.Button("...", (WINDOWWIDTH // 2, WINDOWHEIGHT // 2),
                             font=30, bg="navy", feedback="GAME INIT...")

# start button
button_center.change_text("START GAME")
button_start = Button.Button("START GAME", (WINDOWWIDTH // 2 - button_center.get_size()[0] // 2 + 1,
                                            WINDOWHEIGHT // 2 - button_center.get_size()[1] // 2),
                             font=30, bg="navy", feedback="GAME INIT...")

# button go back
ROW_SEP = 50
button_center.change_text("GO BACK")
button_back = Button.Button("GO BACK", (WINDOWWIDTH // 2 - button_center.get_size()[0] // 2 + 1,
                                            WINDOWHEIGHT // 2 - button_center.get_size()[1] // 2 + ROW_SEP * 2),
                             font=30, bg="navy", feedback="BACK TO MENU...")

# button game 1
button_center.change_text("GAME 1")
button_game1 = Button.Button("GAME 1", (WINDOWWIDTH // 2 - button_center.get_size()[0] // 2 + 1,
                                            WINDOWHEIGHT // 2 - button_center.get_size()[1] // 2 + ROW_SEP * 0),
                             font=30, bg="navy", feedback="LOADING...")
# button game 2
button_center.change_text("GAME 2")
button_game2 = Button.Button("GAME 2", (WINDOWWIDTH // 2 - button_center.get_size()[0] // 2 + 1,
                                            WINDOWHEIGHT // 2 - button_center.get_size()[1] // 2 + ROW_SEP * 1),
                             font=30, bg="navy", feedback="LOADING...")

# button exit a game
button_center.change_text("EXITING...")
button_exit = Button.Button("EXIT", (WINDOWWIDTH - button_center.get_size()[0] // 2, 0),
                             font=30, bg="navy", feedback="EXITING...")


# button QUIT in main menu
button_center.change_text("EXIT")
button_quit = Button.Button("EXIT", (WINDOWWIDTH // 2 - button_center.get_size()[0] // 2 + 1,
                                            WINDOWHEIGHT // 2 - button_center.get_size()[1] // 2 + ROW_SEP * 1),
                             font=30, bg="navy", feedback="EXITING...")

while True:
    bgr = None
    # when in main menu
    if not ingame and not gamemenu:
        bgr = Background1
        DISPLAYSURF.fill((0, 0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            button_start.change_text("START GAME", bg='navy')
            if button_start.click(event):
                gamemenu = True
            if button_quit.click(event):
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(bgr, (0, 0))
        button_start.show(DISPLAYSURF)
        button_quit.show(DISPLAYSURF)
        pygame.display.update()
        fpsClock.tick(FPS)

    # when in game menu
    if gamemenu:
        bgr = Background2
        DISPLAYSURF.fill((0, 0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            button_back.change_text("GO BACK", bg='navy')
            button_game1.change_text("GAME 1", bg='navy')
            button_game2.change_text("GAME 2", bg='navy')
            if button_back.click(event):
                gamemenu = False
            if button_game1.click(event):
                gamemenu = False
                ingame = True
                game = 1
                bgr = game1bg
            if button_game2.click(event):
                gamemenu = False
                ingame = True
                game = 2
                bgr = game2bg

        DISPLAYSURF.blit(bgr, (0, 0))
        button_back.show(DISPLAYSURF)
        button_game1.show(DISPLAYSURF)
        button_game2.show(DISPLAYSURF)
        pygame.display.update()
        fpsClock.tick(FPS)

    # when in game playing
    if ingame:
        up, down, left, right = False, False, False, False
        move_queue = 0
        moving_sprites = pygame.sprite.Group()
        player = Agent.Player(0, 0)
        game_board = maze.Maze(game)
        moving_sprites.add(player)
        while ingame:
            if move_queue == 0:
                if player.is_end:
                    ingame = False
                    gamemenu = True
                if player.col == 23 and player.row == 14:
                    player.terminated()
                    move_queue = 10

                up, down, left, right = False, False, False, False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    button_exit.change_text('EXIT', bg='navy')
                    if button_exit.click(event):
                        gamemenu = True
                        ingame = False
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            operation = SpeechEngine.get_operation(train_set_x, train_set_y)
                            if operation == 'none':
                                pass
                            elif operation == 'trai':
                                player.go_left()
                                if game_board.can_move(player.col - 1, player.row):
                                    player.col -= 1
                                    move_queue = 25
                                    up, down, left, right = False, False, True, False
                            elif operation == 'phai':
                                player.go_right()
                                if game_board.can_move(player.col + 1, player.row):
                                    player.col += 1
                                    move_queue = 25
                                    up, down, left, right = False, False, False, True
                            elif operation == 'len':
                                player.go_up()
                                if game_board.can_move(player.col, player.row - 1):
                                    player.row -= 1
                                    move_queue = 40
                                    up, down, left, right = True, False, False, False
                            elif operation == 'xuong':
                                player.go_down()
                                if game_board.can_move(player.col, player.row + 1):
                                    player.row += 1
                                    move_queue = 40
                                    up, down, left, right = False, True, False, False

            if move_queue > 0:
                player.move(up, down, left, right)
                move_queue -= 1

            # drawing in game
            DISPLAYSURF.fill((0, 0, 0, 0))
            DISPLAYSURF.blit(bgr, (0, 0))
            game_board.draw(DISPLAYSURF)
            button_exit.show(DISPLAYSURF)
            moving_sprites.draw(DISPLAYSURF)
            moving_sprites.update(0.2)
            pygame.display.flip()
            player.draw(DISPLAYSURF)
            pygame.display.update()
            fpsClock.tick(FPS)
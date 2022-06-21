import pygame, sys
import numpy as np


class Maze:
    def __init__(self, num_maze):
        self.M = 15
        self.N = 24
        self.maze = self.txt_to_numpy('./maze/' + str(num_maze) + '.txt')
        self.img = pygame.image.load('./maze/brick.jpg')
        self.img = pygame.transform.scale(self.img, (25, 40))
        self.end = pygame.image.load('./maze/start.png')
        self.end = pygame.transform.scale(self.end, (25, 40))
        self.start = pygame.image.load('./maze/end.png')
        self.start = pygame.transform.scale(self.start, (25, 40))

    def draw(self, screen):
        screen.blit(self.start, (0, 0))
        for i in range(self.M):
            for j in range(self.N):
                if self.maze[i][j] == 1:
                    screen.blit(self.img, (j * 25, i * 40))
                elif self.maze[i][j] == 2:
                    screen.blit(self.end, (j * 25, i * 40))


    def can_move(self, x, y):
        if x < 0 or x > 23:
            return False
        if y < 0 or y > 14:
            return False
        if self.maze[y][x] == 1:
            return False
        return True


    def txt_to_numpy(self, path):
        board = np.zeros((15, 24))
        i = 0
        with open(path) as fp:
            Lines = fp.readlines()
            for line in Lines:
                lst = []
                for ch in line.strip():
                    if ch == '#':
                        lst.append(1)
                    elif ch == '.':
                        lst.append(0)
                    elif ch == 'o':
                        lst.append(2)
                board[i] = np.array(lst)
                i += 1
        return board
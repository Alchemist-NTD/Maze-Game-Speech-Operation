import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.move_left, self.move_right, self.move_up, self.move_down, self.is_end \
            = False, False, False, False, False
        self.sprites_left = [pygame.image.load('./img/agent/l' + str(i) + '.gif') for i in range(5)]
        self.sprites_down = [pygame.image.load('./img/agent/d' + str(i) + '.gif') for i in range(5)]
        self.sprites_right = [pygame.image.load('./img/agent/r' + str(i) + '.gif') for i in range(5)]
        self.sprites_up = [pygame.image.load('./img/agent/u' + str(i) + '.gif') for i in range(5)]
        self.sprites_dead = [pygame.image.load('./img/agent/t' + str(i) + '.gif') for i in range(5)]
        self.sprites = self.sprites_down
        self.current_sprite = 0
        self.image = self.sprites_down[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (25, 40))
        self.col, self.row = int(pos_x / 25), int(pos_y / 40)
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def go_left(self):
        self.move_left = True
        self.sprites = self.sprites_left

    def go_right(self):
        self.move_right = True
        self.sprites = self.sprites_right

    def go_up(self):
        self.move_left = True
        self.sprites = self.sprites_up

    def go_down(self):
        self.move_down = True
        self.sprites = self.sprites_down

    def terminated(self):
        self.is_end = True
        self.sprites = self.sprites_dead

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, speed):
        if self.move_left:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.move_left = False

        if self.move_right:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.move_right = False

        if self.move_up:
            self.current_sprite += (speed - 0.15)
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.move_up = False

        if self.move_down:
            self.current_sprite += (speed - 0.09)
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.move_down = False

        if self.is_end:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.is_end = False

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, (25, 40))


    def move(self, up, down, left, right):
        WINDOWHEIGHT = 600
        WINDOWWIDTH = 600
        if up:
            if self.rect.top <= 0:
                self.rect.top = 0
                return
            self.rect.centery -= 1
        if down:
            if self.rect.bottom >= WINDOWHEIGHT:
                self.rect.bottom = WINDOWHEIGHT
                return
            self.rect.centery += 1
        if left:
            if self.rect.left <= 0:
                self.rect.left = 0
                return
            self.rect.centerx -= 1
        if right:
            if self.rect.right >= WINDOWWIDTH:
                self.rect.right = WINDOWWIDTH
                return
            self.rect.centerx += 1

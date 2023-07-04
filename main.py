import pygame
class Sprite:
    def __init__(self, x, y, speed, img):
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.speed = speed
        self.x = x
        self.y = y
        self.imgR = self.image
        self.imgL = pygame.transform.flip(self.image, True, False)

    def cords(self):
        return tuple([self.x, self.y])

    def move(self, side):
        if side == 'right':
            self.x += self.speed
            self.image = self.imgL
        elif side == 'left':
            self.x -= self.speed
            self.image = self.imgR
        elif side == 'up':
            self.x += self.speed
        elif side == 'down':
            self.x -= self.speed


w = pygame.display.set_mode((1279, 700))
Player = Sprite(100, 100, 1, '12345/qwerty.jpg')
game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.move('right')
    if keys[pygame.K_LEFT]:
        Player.move('left')
    w.fill((0, 0, 0))
    w.blit(Player.image, Player.cords())
    pygame.display.update()
pygame.quit()
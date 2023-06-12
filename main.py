import sys
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/player_car.png")
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2()
        self.speed = 4

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position.x -= self.speed
        if keys[pygame.K_d]:
            self.position.x += self.speed

        self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Background():
    def __init__(self, screen_width, screen_height):
        self.bgimage = pygame.image.load("sprites/background.png")
        self.rectBGimg = self.bgimage.get_rect()

        self.backgroundY1 = 0
        self.backgroundX1 = 0

        self.backgroundY2 = -self.rectBGimg.height
        self.backgroundX2 = - 0

        self.moving_speed = 5

        self.screen_width = screen_width
        self.screen_height = screen_height

        # Stretch the first instance of the background image
        self.bgimage_stretched = pygame.transform.scale(self.bgimage, (self.screen_width, self.rectBGimg.height))

    def update(self):
        self.backgroundY1 += self.moving_speed
        self.backgroundY2 += self.moving_speed

        if self.backgroundY1 >= self.screen_height:
            self.backgroundY1 = self.backgroundY2 - self.rectBGimg.height

        if self.backgroundY2 >= self.screen_height:
            self.backgroundY2 = self.backgroundY1 - self.rectBGimg.height

    def render(self, screen):
        screen.blit(self.bgimage_stretched, (self.backgroundX1, self.backgroundY1))
        screen.blit(self.bgimage, (self.backgroundX2, self.backgroundY2))



def main():
    pygame.init()
    pygame.display.set_caption("CarGoVroom")

    screen_width = 700
    screen_height = 780
    screen = pygame.display.set_mode((screen_width, screen_height))

    player_car = Player()
    background = Background(screen_width, screen_height)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player_car)

    player_car.position.y = screen_height - 100
    player_car.position.x = screen_width // 2

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_car.update()
        background.update()

        screen.fill((0, 1, 0))
        background.render(screen)

        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

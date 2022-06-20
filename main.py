import pygame
import os

WIDTH = 900
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)

SHOOTER_IMAGE = pygame.image.load(os.path.join(
    "zombie-shooter", "Assets", "main_shooter.png"))
SHOOTER = pygame.transform.scale(SHOOTER_IMAGE, (60, 50))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Shooter")

class Shooter:
    def __init__(self) -> None:
        self.x = 400
        self.y = 320
        self.width = 60
        self.height = 50
        self.speed = 10
    
    def draw(self):
        shooter = pygame.Rect(self.x, self.y, self.width, self.height)
        WIN.blit(SHOOTER, (shooter.x, shooter.y))

    def handle_move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.x - self.speed - 5 > 0:
            self.x -= self.speed
        if keys_pressed[pygame.K_d] and self.x + self.speed + 55 < WIDTH:
            self.x += self.speed
        if keys_pressed[pygame.K_w] and self.y - self.speed - 5 > 0:
            self.y -= self.speed
        if keys_pressed[pygame.K_s] and self.y + self.speed + 45 < HEIGHT:
            self.y += self.speed


def draw_screen():
    WIN.fill(WHITE)


def main():
    shooter = Shooter()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_screen()
        shooter.draw()
        pygame.display.update()
        
        shooter.handle_move()
    
    pygame.quit()


if __name__ == '__main__':
    main()

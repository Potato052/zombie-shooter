import pygame
import os

WIDTH = 900
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)

SHOOTER_IMAGE = pygame.image.load(os.path.join("Assets", "main_shooter.png"))
SHOOTER = pygame.transform.scale(SHOOTER_IMAGE, (60, 50))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("10 minutes till dawn")

def draw_screen(shooter):
    WIN.fill(WHITE)
    WIN.blit(SHOOTER, (shooter.x, shooter.y))
    pygame.display.update()


def main():
    shooter = pygame.Rect(400, 320, 60, 50)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys=pressed = pygame.key.get_pressed()
         
        draw_screen(shooter)
    pygame.quit()




if __name__ == '__main__':
    main()
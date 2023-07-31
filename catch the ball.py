import pygame
import random
import sys


# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 120, 10
BALL_RADIUS = 10
PADDLE_SPEED = 10
BALL_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_paddle(x):
    pygame.draw.rect(window, WHITE, (x, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_ball(x, y):
    pygame.draw.circle(window, RED, (x, y), BALL_RADIUS)

def is_collision(ball_x, ball_y, paddle_x):
    return ball_x >= paddle_x and ball_x <= paddle_x + PADDLE_WIDTH and ball_y >= HEIGHT - PADDLE_HEIGHT - BALL_RADIUS

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over!", True, RED)
    window.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)

def game_loop():
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    ball_x, ball_y = random.randint(0, WIDTH), BALL_RADIUS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
            paddle_x += PADDLE_SPEED

        ball_y += BALL_SPEED

        window.fill(BLACK)
        draw_paddle(paddle_x)
        draw_ball(ball_x, ball_y)

        if ball_y >= HEIGHT - BALL_RADIUS:
            if is_collision(ball_x, ball_y, paddle_x):
                ball_y = BALL_RADIUS
                ball_x = random.randint(0, WIDTH)
            else:
                game_over()
                game_loop()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()

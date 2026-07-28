import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_loop():
    snake = [[100, 100]]
    direction = "RIGHT"
    food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
    score = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
        
        head = snake[0].copy()
        if direction == "UP": head[1] -= CELL_SIZE
        elif direction == "DOWN": head[1] += CELL_SIZE
        elif direction == "LEFT": head[0] -= CELL_SIZE
        elif direction == "RIGHT": head[0] += CELL_SIZE
        
        snake.insert(0, head)
        
        if head == food:
            score += 10
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            snake.pop()
        
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            running = False
        
        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        show_score(score)
        pygame.display.flip()
        clock.tick(FPS)
    
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()

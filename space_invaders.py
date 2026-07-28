import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 80
player_speed = 5

# Bullets
bullets = []
bullet_speed = 7

# Enemies
enemies = []
enemy_width = 40
enemy_height = 30
enemy_speed = 2
enemy_direction = 1

for row in range(5):
    for col in range(10):
        x = 80 + col * 60
        y = 50 + row * 50
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_x + player_width//2 - 2, player_y, 4, 10)
                bullets.append(bullet)
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # Move bullets
    for bullet in bullets[: ]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Move enemies
    move_down = False
    for enemy in enemies:
        enemy.x += enemy_speed * enemy_direction
        if enemy.x <= 0 or enemy.x >= WIDTH - enemy_width:
            move_down = True
    if move_down:
        enemy_direction *= -1
        for enemy in enemies:
            enemy.y += 20
    
    # Check collisions
    for bullet in bullets[: ]:
        for enemy in enemies[: ]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break
    
    # Draw everything
    draw_player(player_x, player_y)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    # Score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Win condition
    if not enemies:
        win_text = font.render('YOU WIN!', True, GREEN)
        screen.blit(win_text, (WIDTH//2 - 60, HEIGHT//2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
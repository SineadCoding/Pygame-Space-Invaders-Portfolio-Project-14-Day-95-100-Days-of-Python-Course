import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 700
width, height = 550, 700
w, h = 650, 700
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders - By Sinead Coding')

font = pygame.font.SysFont("Atari", 25)

clock = pygame.time.Clock()

background = pygame.image.load('content/background.jpg')

logo = pygame.transform.scale(pygame.image.load('content/logo.png'), (160, 80))

line = pygame.transform.scale(pygame.image.load('content/line.png'), (450, 10))

score = 0
score_tag = font.render(f"Score: {score}", True, WHITE)

life_count = 3
life = pygame.transform.scale(pygame.image.load('content/heart.png'), (30, 30))

alien_count = 8
alien_1 = pygame.transform.scale(pygame.image.load('content/alien 1.png'), (20, 20))

alien_3 = pygame.transform.scale(pygame.image.load('content/alien 3.png'), (30, 30))

alien_1_walk = pygame.transform.scale(pygame.image.load('content/alien_1_walk.png'), (20, 20))
alien_3_walk = pygame.transform.scale(pygame.image.load('content/alien_3_walk.png'), (25, 25))

rocket_1 = pygame.transform.scale(pygame.image.load('content/rocket.png'), (25, 30))
rocket_2 = pygame.transform.scale(pygame.image.load('content/rocket.png'), (25, 30))
rocket_3 = pygame.transform.scale(pygame.image.load('content/rocket.png'), (25, 30))

block = pygame.transform.scale(pygame.image.load('content/block.png'), (5, 30))

earth = pygame.transform.scale(pygame.image.load('content/earth.png'), (40, 40))

bullet_image = pygame.transform.scale(pygame.image.load('content/bullet.png'), (5, 10))

alien_bullet_image = pygame.transform.scale(pygame.image.load('content/bullet.png'), (5, 10))


class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx):
        if 0 <= self.x + dx <= WIDTH - rocket_1.get_width():
            self.x += dx


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y -= self.speed


class AlienBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        self.y += self.speed


class Alien:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.shoot_time = random.randint(1000, 5000)
        self.last_shot = pygame.time.get_ticks()

    def draw(self, walk_frame):
        if self.type == 1:
            if walk_frame == 0:
                screen.blit(alien_1, (self.x, self.y))
            else:
                screen.blit(alien_1_walk, (self.x, self.y))
        elif self.type == 3:
            if walk_frame == 0:
                screen.blit(alien_3, (self.x, self.y))
            else:
                screen.blit(alien_3_walk, (self.x, self.y))

    def move(self, dx):
        self.x += dx

    def shoot(self, alien_bullets):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.shoot_time:
            alien_bullets.append(AlienBullet(self.x + alien_1.get_width() // 2, self.y))
            self.last_shot = current_time
            self.shoot_time = random.randint(2000, 10000)


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = block

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def create_aliens():
    aliens = []
    space = 150
    # aliens.append(Alien(255, 160, 2))
    for _ in range(alien_count):
        space += 30
        aliens.append(Alien(space, 230, 1))
        aliens.append(Alien(space, 260, 1))
        aliens.append(Alien(space - 5, 290, 3))
    return aliens


def create_blocks():
    blocks = []
    for x in range(100, 490, 5):
        for y in range(380, 460, 20):
            blocks.append(Block(x, y))
    return blocks


def draw_text(text, x, y, size=25):
    font_size = pygame.font.SysFont("Atari", size)
    text_surface = font_size.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))


def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 1)
    pygame.draw.rect(screen, (200, 200, 200), (x + 5, y + 5, width - 10, height - 10))
    draw_text(text, x + 20, y + 15)


def main():
    running = True
    rockets = [Rocket(60, 580), Rocket(60, 630), Rocket(120, 630)]
    current_rocket = 0
    speed = 5
    bullets = []
    alien_bullets = []
    aliens = create_aliens()
    blocks = create_blocks()
    alien_speed = 1.5
    alien_direction = 1
    global score
    game_over = False
    game_won = False
    walk_frame = 0
    walk_frame_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(
                        Bullet(rockets[current_rocket].x + rocket_1.get_width() // 2, rockets[current_rocket].y))
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                mouse_x, mouse_y = event.pos
                if 250 < mouse_x < 350 and 400 < mouse_y < 450:
                    game_over = False
                    game_won = False
                    rockets = [Rocket(60, 580), Rocket(60, 630), Rocket(120, 630)]
                    current_rocket = 0
                    speed = 5
                    bullets = []
                    alien_bullets = []
                    aliens = create_aliens()
                    blocks = create_blocks()
                    alien_speed = 1.5
                    alien_direction = 1
                    score = 0
                    walk_frame = 0
                    walk_frame_time = pygame.time.get_ticks()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not game_over:
            rockets[current_rocket].move(-speed)
        if keys[pygame.K_RIGHT] and not game_over:
            rockets[current_rocket].move(speed)

        screen.blit(background, (0, 0))

        if not game_over:
            screen.blit(logo, (220, 30))
            screen.blit(line, (70, 115))
            draw_text(f"Score: {score}", 115, 135)
            screen.blit(line, (50, 620))

            for i, rocket in enumerate(rockets):
                if i == current_rocket:
                    screen.blit(rocket_1, (rocket.x, 580))
                else:
                    screen.blit(rocket_1, (rocket.x, rocket.y))

            for bullet in bullets:
                screen.blit(bullet_image, (bullet.x, bullet.y))
                bullet.move()
                if bullet.y < 0:
                    bullets.remove(bullet)

            for alien_bullet in alien_bullets:
                screen.blit(alien_bullet_image, (alien_bullet.x, alien_bullet.y))
                alien_bullet.move()
                if alien_bullet.y > HEIGHT:
                    alien_bullets.remove(alien_bullet)

                if (rockets[current_rocket].x < alien_bullet.x < rockets[current_rocket].x + rocket_1.get_width() and
                        580 < alien_bullet.y < 580 + rocket_1.get_height()):
                    alien_bullets.remove(alien_bullet)
                    if current_rocket < len(rockets) - 1:
                        current_rocket += 1
                        rockets[current_rocket - 1].x = -100
                        rockets[current_rocket - 1].y = -100
                        rockets[current_rocket].x = 60
                        rockets[current_rocket].y = 630
                    else:
                        game_over = True
                        game_won = False

            min_x = min(alien.x for alien in aliens)
            max_x = max(alien.x for alien in aliens)
            if min_x < 20 or max_x > WIDTH - 20 - alien_1.get_width():
                alien_direction *= -1
            current_time = pygame.time.get_ticks()
            if current_time - walk_frame_time >= 200:  # switch frames every 200ms
                walk_frame = (walk_frame + 1) % 2
                walk_frame_time = current_time
            for alien in aliens:
                alien.move(alien_speed * alien_direction)
                alien.draw(walk_frame)
                alien.shoot(alien_bullets)

                for bullet in bullets:
                    if (alien.x < bullet.x < alien.x + alien_1.get_width() and
                            alien.y < bullet.y < alien.y + alien_1.get_height()):
                        if alien.type == 2:
                            score += 15
                        else:
                            score += 10
                        aliens.remove(alien)
                        bullets.remove(bullet)
                        if len(aliens) == 0:
                            game_over = True
                            game_won = True

            for block in blocks:
                block.draw()
                for bullet in bullets:
                    if (block.x < bullet.x < block.x + block.image.get_width() and
                            block.y < bullet.y < block.y + block.image.get_height()):
                        blocks.remove(block)
                        bullets.remove(bullet)
                        score += 2

                for alien_bullet in alien_bullets:
                    if (block.x < alien_bullet.x < block.x + block.image.get_width() and
                            block.y < alien_bullet.y < block.y + block.image.get_height()):
                        blocks.remove(block)
                        alien_bullets.remove(alien_bullet)
        else:
            large_logo = pygame.transform.scale(logo, (320, 160))
            screen.blit(large_logo, (140, 50))
            if game_won:
                draw_text("Game Over - YOU WON!", width // 2 - 150, height // 2 - 25, 50)
            else:
                draw_text("Game Over - YOU LOST!", width // 2 - 150, height // 2 - 25, 50)
            draw_text(f"Your score is: {score}", w // 2 - 100, h // 2 + 25, 30)
            draw_button("Replay", 250, 400, 100, 50)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

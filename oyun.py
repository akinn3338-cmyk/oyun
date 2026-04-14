import pygame
import pymunk

# Initialize Pygame
pygame.init()

# Game Variables
score = 0
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Physics Setup
space = pymunk.Space()
space.gravity = (0, 900)

# Ragdoll Class
class Ragdoll:
    def __init__(self, x, y):
        self.body = pymunk.Body(1, pymunk.moment_for_box(1, 50, 50))
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body)
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.body.position.x, self.body.position.y, 50, 50))

# Create the Ragdoll
ragdoll = Ragdoll(400, 300)

# Questions
questions = [
    ('Is Python a programming language?', True),
    ('Is 2 + 2 equal to 5?', False),
    ('Is the Earth flat?', False),
    ('Do we need to breathe oxygen?', True),
    ('Is Pygame used for game development?', True),
    ('Can we see infrared light?', False),
    ('Is the sun a star?', True),
    ('Is water wet?', True),
    ('Is HTML a programming language?', False),
    ('Does sound travel faster in water?', True)
]

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Physics
    space.step(1/50.0)

    # Draw
    screen.fill((255, 255, 255))
    ragdoll.draw()

    # Score display
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
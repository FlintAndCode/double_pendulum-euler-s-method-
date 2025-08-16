import pygame
import math
from sys import exit


def returner(alpha, betta, omega1, omega2):
        a1 = ((-3 * g * math.sin(alpha) - g * math.sin(alpha - 2 * betta) 
        - 2 * math.sin(alpha - betta) * (omega2**2 * length + omega1**2 * length * math.cos(alpha - betta)))
        / (length * (3 - math.cos(2 * (alpha - betta)))))

        a2 = ((2 * math.sin(alpha - betta) * (omega1**2 * length * 2 + 2 * g * math.cos(alpha) + omega2**2 * length * math.cos(alpha - betta)))
            /(length * (3 - math.cos(2 * (alpha - betta)))))
        return a1, a2

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pendulum Simulation")
clock = pygame.time.Clock()
alpha = math.radians(60)
betta = math.radians(140)  
length = 50
g = 5.81
omega1 = 0
omega2 = 0
angular_acc = 0
t = 0.06

pivot_x = 400
pivot_y = 100

trail1 = []
trail2 = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    a1, a2 = returner(alpha, betta, omega1, omega2)
    omega1 += a1 * t
    omega2 += a2 * t    
    alpha += omega1 * t 
    betta += omega2 * t

    omega1 *= 1.0001
    omega2 *= 1.0001
    
    x1 = pivot_x + length * math.sin(alpha)
    y1 = pivot_y + length * math.cos(alpha)
    x2 = x1 + length * math.sin(betta)
    y2 = y1 + length * math.cos(betta)
    
    trail1.append((x1, y1))
    trail2.append((x2, y2))
    
    if len(trail1) > 1000:
        trail1.pop(0)
    if len(trail2) > 1000:
        trail2.pop(0)
    
    screen.fill('Black')
    
    for pos in trail1:
        pygame.draw.circle(screen, 'Red', (int(pos[0]), int(pos[1])), 1)
    for pos in trail2:
        pygame.draw.circle(screen, 'Blue', (int(pos[0]), int(pos[1])), 1)
    
    pygame.draw.line(screen, 'White', (pivot_x, pivot_y), (int(x1), int(y1)), 1)
    pygame.draw.circle(screen, 'Red', (int(x1), int(y1)), 10)
    pygame.draw.line(screen, 'White', (int(x1), int(y1)), (int(x2), int(y2)), 1)
    pygame.draw.circle(screen, 'Blue', (int(x2), int(y2)), 10)
    pygame.display.update()
    clock.tick(80)  
    


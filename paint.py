# Imports
import pygame

# Initialising pyGame
pygame.init()

# Assigning window data variables
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Assigning colour choices
active_size = 0
active_colour = ("white")

# Assigning window variable to render window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()

# Setting window title and font variables
font = pygame.font.Font("freesansbold.ttf", 40)
small_font = pygame.font.Font("freesansbold.ttf", 20)
pygame.display.set_caption("RGB Colour Picker")

# Menu render function
def draw_menu():
    # Menu background
    pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])
    pygame.draw.line(screen, "black", (0, 70), (WIDTH, 70), 2)

    # Brush buttons
    s_brush = pygame.draw.rect(screen, "black", [10, 10, 50, 50])
    pygame.draw.circle(screen, "white", (35, 35), 5)

    m_brush = pygame.draw.rect(screen, "black", [85, 10, 50, 50])
    pygame.draw.circle(screen, "white", (110, 35), 10)

    l_brush = pygame.draw.rect(screen, "black", [160, 10, 50, 50])
    pygame.draw.circle(screen, "white", (185, 35), 15)

    xl_brush = pygame.draw.rect(screen, "black", [235, 10, 50, 50])
    pygame.draw.circle(screen, "white", (260, 35), 20)

    # Colour buttons
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 10, 25, 25])
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 60, 35, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 35, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (175, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])

    # Assigning choices into lists
    brush_list = [s_brush, m_brush, l_brush, xl_brush]
    colour_choice = [red, green, blue, teal, purple, black, white]

    rgb_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (175, 0, 255), (0, 0, 0), (255, 255, 255)]
    return brush_list, colour_choice, rgb_list

# Game will run while "running" is true
running = True
while running:
    # Setting refresh rate of game
    timer.tick(FPS)
    # Filling screen to black
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_colour, mouse, active_size)
    brushes, colours, rgbs = draw_menu()

    for event in pygame.event.get():
        # If close window button pressed, game will quit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            for i in range(len(colours)):
                if colours[i].collidepoint(event.pos):
                    active_colour = rgbs[i]

    # Updating display
    pygame.display.flip()

# Exits game
pygame.quit()

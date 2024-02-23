import pygame, sys
from button import Button

WIDTH = 1280
HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Vibrant Ventures")

BG = pygame.image.load("assets/Background.png")

# Returns Press-Start-2P in the desired size
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

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

def play():
    
    active_size = 0
    active_colour = ("white")
    
    while True:

        # Filling screen to white
        screen.fill("white")
        # Getting mouse position
        mouse = pygame.mouse.get_pos()
        # Ensures that paint is rendered while hovering the canvas
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
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
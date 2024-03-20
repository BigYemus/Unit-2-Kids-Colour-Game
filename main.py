import pygame
import sys
import tkinter as tk
from tkinter import StringVar
from PIL import Image, ImageTk

from button import Button

pygame.init()

screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
FPS = 244
picture = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(picture, (WIDTH, HEIGHT))
painting = []

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Vibrant Ventures")
timer = pygame.time.Clock()

# Defining and assigning variables to track what the current question is and count the correct answers.
index = 0
correct_answers = 0


# Defining font for the menu and character design part of the game.
def get_font(size):
    return pygame.font.Font("assets/SpicyRice-Regular.ttf", size)


# Menu function
def draw_menu(size, active_colour):
    # Menu background
    pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])
    pygame.draw.line(screen, "black", (0, 70), (WIDTH, 70), 2)

    pygame.draw.rect(screen, "gray", [0, HEIGHT - 70, WIDTH, HEIGHT - 70])
    pygame.draw.line(screen, "black", (0, HEIGHT - 70), (WIDTH, HEIGHT - 70), 2)

    # Brush buttons
    s_brush = pygame.draw.rect(screen, "gray", [10, 10, 50, 50])
    pygame.draw.circle(screen, "white", (35, 35), 5)

    m_brush = pygame.draw.rect(screen, "gray", [85, 10, 50, 50])
    pygame.draw.circle(screen, "white", (110, 35), 10)

    l_brush = pygame.draw.rect(screen, "gray", [160, 10, 50, 50])
    pygame.draw.circle(screen, "white", (185, 35), 15)

    xl_brush = pygame.draw.rect(screen, "gray", [235, 10, 50, 50])
    pygame.draw.circle(screen, "white", (260, 35), 20)

    # Character design text
    character_text = get_font(30).render("Design your Character!", True, "black")
    character_text_rect = character_text.get_rect(center=(WIDTH / 2, 35))
    screen.blit(character_text, character_text_rect)

    # Colour buttons
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 10, 25, 25])
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 60, 35, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 35, 35, 25, 25])
    cyan = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (175, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])

    # Highlighting selected brush size
    if size == 5:
        pygame.draw.circle(screen, "black", (35, 35), 5, 3)
    elif size == 10:
        pygame.draw.circle(screen, "black", (110, 35), 10, 3)
    elif size == 15:
        pygame.draw.circle(screen, "black", (185, 35), 15, 3)
    elif size == 20:
        pygame.draw.circle(screen, "black", (260, 35), 20, 3)

    # Highlighting selected colour
    if active_colour == (255, 0, 0):
        pygame.draw.rect(screen, "pink", [WIDTH - 60, 10, 25, 25], 3)
    if active_colour == (0, 255, 0):
        pygame.draw.rect(screen, "pink", [WIDTH - 35, 10, 25, 25], 3)
    if active_colour == (0, 0, 255):
        pygame.draw.rect(screen, "pink", [WIDTH - 60, 35, 25, 25], 3)
    if active_colour == (255, 255, 0):
        pygame.draw.rect(screen, "pink", [WIDTH - 35, 35, 25, 25], 3)
    if active_colour == (0, 255, 255):
        pygame.draw.rect(screen, "pink", [WIDTH - 85, 10, 25, 25], 3)
    if active_colour == (175, 0, 255):
        pygame.draw.rect(screen, "pink", [WIDTH - 85, 35, 25, 25], 3)
    if active_colour == (0, 0, 0):
        pygame.draw.rect(screen, "pink", [WIDTH - 110, 10, 25, 25], 3)
    if active_colour == (255, 255, 255):
        pygame.draw.rect(screen, "pink", [WIDTH - 110, 35, 25, 25], 3)

    # Assigning choices into lists
    brush_list = [s_brush, m_brush, l_brush, xl_brush]
    colour_choice = [red, green, blue,
                     yellow, cyan, purple, black, white]

    # Storing choices into variables
    rgb_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (175, 0, 255), (0, 0, 0),
                (255, 255, 255)]

    return brush_list, colour_choice, rgb_list


# Function to start character design
def play():
    # Defining choice variables
    active_size = 0
    active_colour = "white"

    while True:
        # Setting FPS
        timer.tick(FPS)

        # Filling screen to white
        screen.fill("white")

        # Getting mouse position
        mouse = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and mouse[1] > 70 and left_click and mouse[1] < HEIGHT - 70:
            painting.append((active_colour, mouse, active_size))
        draw_painting(painting)
        # Ensures that paint is rendered while hovering the canvas
        if 70 < mouse[1] < HEIGHT - 70:
            pygame.draw.circle(screen, active_colour, mouse, active_size)
        brushes, colours, rgbs = draw_menu(active_size, active_colour)

        # defining buttons
        back_button = Button(image=None, pos=(60, HEIGHT - 35),
                             text_input="Back", font=get_font(20), base_color="black", hovering_color="White")
        next_button = Button(image=None, pos=(WIDTH - 60, HEIGHT - 35),
                             text_input="Next", font=get_font(20), base_color="black", hovering_color="White")

        # Button functionality
        mouse_position = pygame.mouse.get_pos()

        for button in [back_button, next_button]:
            button.changeColor(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            # If mouse is clicked on brush size option, game will select option
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(brushes)):
                    if brushes[i].collidepoint(event.pos):
                        active_size = (i * 5) + 5
                # If mouse is clicked on brush colour option, game will select option
                for i in range(len(colours)):
                    if colours[i].collidepoint(event.pos):
                        active_colour = rgbs[i]
            # If close window button pressed, game will quit
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.checkForInput(mouse_position):
                    pygame.quit()
                    questions()
                if back_button.checkForInput(mouse_position):
                    main_menu()

        # Updating display
        pygame.display.update()


def draw_painting(paints):
    # Will render selected brush size and colour onto the canvas
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])


# Function to start the multiple choice part
def questions():
    # Defining window parameters
    res = str(WIDTH) + "x" + str(HEIGHT)
    root = tk.Tk()
    root.geometry(res)
    root.attributes('-fullscreen', True)
    root.configure(bg="#EDFCFF")
    root.title("Vibrant Ventures")

    # Defining the frame for the widgets to be placed in
    frame = tk.Frame(root, width=WIDTH)

    # Configuring the above defined frame
    root.columnconfigure(index=0, weight=1)
    root.rowconfigure(index=0, weight=1)

    # Library of questions
    questions = [
        "This shape needs help! Can you guess what shape this is?",
        "Circle is stuck! How many corners does Circle have?",
        "Pentagon has lost track! How many points does Pentagon have?",
        "Square is confused! What other shape has as many sides as Square?"]

    # library of answers
    options = [["Triangle", "Rectangle", "Circle", "Square"],
               ["2", "5", "0", "1"],
               ["10", "2", "6", "5"],
               ["Circle", "Diamond", "Octagon", "Blue"]]

    # Importing images for characters to be displayed
    scene_image1 = Image.open("assets/scene1.png").resize((250, 250))
    scene_image_tk1 = ImageTk.PhotoImage(scene_image1)
    scene_image2 = Image.open("assets/scene2.png").resize((250, 250))
    scene_image_tk2 = ImageTk.PhotoImage(scene_image2)
    scene_image3 = Image.open("assets/scene3.png").resize((250, 250))
    scene_image_tk3 = ImageTk.PhotoImage(scene_image3)
    scene_image4 = Image.open("assets/scene4.png").resize((250, 250))
    scene_image_tk4 = ImageTk.PhotoImage(scene_image4)

    # Assigning each question option to a variable.
    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)
    v4 = StringVar(frame)

    # Defining the widgets, along with styling options and their commands.
    button_width = str(WIDTH // 50)
    button_height = str(HEIGHT // 300)

    scene_widget = tk.Label(frame, image=scene_image_tk1, bd=None, bg="#EDFCFF")
    question_title = tk.Label(frame, bg="#EDFCFF", font=("Ubuntu", 16), wraplength=WIDTH / 3)

    option_1 = tk.Radiobutton(frame, bg="#ffb3ba", width=button_width, height=button_height,
                              font=("Ubuntu", 18, "bold"), variable=v1, indicatoron=0,
                              command=lambda: check_answer(option_1))
    option_2 = tk.Radiobutton(frame, bg="#ffdfba", width=button_width, height=button_height,
                              font=("Ubuntu", 18, "bold"), variable=v2, indicatoron=0,
                              command=lambda: check_answer(option_2))
    option_3 = tk.Radiobutton(frame, bg="#ffffba", width=button_width, height=button_height,
                              font=("Ubuntu", 18, "bold"), variable=v3, indicatoron=0,
                              command=lambda: check_answer(option_3))
    option_4 = tk.Radiobutton(frame, bg="#baffc9", width=button_width, height=button_height,
                              font=("Ubuntu", 18, "bold"), variable=v4, indicatoron=0,
                              command=lambda: check_answer(option_4))

    button_next = tk.Button(frame, bg="#fff", height=button_height, font=("Ubuntu", 16), text="Next",
                            command=lambda: next_question())

    # Setting position of each element using Tkinter's grid
    frame.pack(expand=True)

    scene_widget.grid(sticky="NESW", row=0, column=0, columnspan=2, bd=None)
    question_title.grid(sticky="NESW", row=1, column=0, columnspan=2)

    option_1.grid(sticky="NESW", row=2, column=0)
    option_2.grid(sticky="NESW", row=2, column=1)
    option_3.grid(sticky="NESW", row=3, column=0)
    option_4.grid(sticky="NESW", row=3, column=1)

    button_next.grid(sticky="NESW", row=4, column=0, columnspan=2, bd=None)

    # Function to disable question options
    def disable_buttons(state):
        option_1["state"] = state
        option_2["state"] = state
        option_3["state"] = state
        option_4["state"] = state

    # Function to check answer
    def check_answer(radio):
        # Making variables global to use within function
        global correct_answers, index

        # Checking if the option selected is equal to the correct answer
        if index == 0:
            if radio["text"] == "Triangle":
                correct_answers += 1
        if index == 1:
            if radio["text"] == "0":
                correct_answers += 1
        if index == 2:
            if radio["text"] == "5":
                correct_answers += 1
        if index == 3:
            if radio["text"] == "Diamond":
                correct_answers += 1

        # Disabling the options once one is selected and keeping track of the question number
        index += 1
        disable_buttons("disable")

    # Function to display next question.
    def next_question():
        # Making variables global to use within function
        global index, correct_answers

        # Destroying the window if user chooses to quit
        if button_next["text"] == "Quit Game":
            root.destroy()

        # Will display overall score if index has reached the last question while prompting the user to quit
        if index == len(options):
            question_title["text"] = "You have scored " + str(correct_answers) + " / " + str(
                len(options)) + " questions!"
            button_next["text"] = "Quit Game"

        # Cycles through all questions and choices
        else:
            question_title["text"] = questions[index]

            # Enables choices
            disable_buttons("normal")

            # Assigning options index to a variable
            opts = options[index]

            # Assigning each option to each choice button
            option_1["text"] = opts[0]
            option_2["text"] = opts[1]
            option_3["text"] = opts[2]
            option_4["text"] = opts[3]

            # Setting the choices and image to display within the GUI
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])
            v4.set(opts[3])

            # Running the image change function to change character on the screen
            image_change()

            # Will change the button to "Check Results" if the user reaches the final question
            if index == len(options) - 1:
                button_next["text"] = "Check results"

    # Function to change scene image depending on question
    def image_change():
        if index == 1:
            scene_widget["image"] = scene_image_tk2
        elif index == 2:
            scene_widget["image"] = scene_image_tk3
        elif index == 3:
            scene_widget["image"] = scene_image_tk4

    # Calling functions
    next_question()
    root.mainloop()


def settings():
    # Making variables global to use within function
    global WIDTH, HEIGHT

    while True:
        # Gets position of the mouse
        mouse_position = pygame.mouse.get_pos()

        # Renders white screen of menu
        screen.fill("white")

        # Defining buttons that allow user to set game to windowed or fullscreen
        windowed_btn = Button(image=pygame.image.load("assets/Windowed Rect.png"), pos=(WIDTH / 2, HEIGHT - 600),
                              text_input="Windowed", font=get_font(40), base_color="black", hovering_color="gray")

        fullscreen_btn = Button(image=pygame.image.load("assets/Fullscreen Rect.png"), pos=(WIDTH / 2, HEIGHT - 450),
                                text_input="Fullscreen", font=get_font(40), base_color="black", hovering_color="gray")

        # defining button to return to main menu
        back_btn = Button(image=None, pos=(WIDTH / 2, (HEIGHT / 2) * 1.5),
                          text_input="BACK", font=get_font(75), base_color="Black", hovering_color="gray")

        # Rendering all buttons onto screen and changing colour while hovering
        back_btn.changeColor(mouse_position)
        back_btn.update(screen)

        windowed_btn.changeColor(mouse_position)
        windowed_btn.update(screen)

        fullscreen_btn.changeColor(mouse_position)
        fullscreen_btn.update(screen)

        for event in pygame.event.get():
            # If close window button pressed, game will quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If mouse is clicked on back button, game will run main menu function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.checkForInput(mouse_position):
                    main_menu()
                # If mouse is clicked on fullscreen button, game will set window to fullscreen
                if windowed_btn.checkForInput(mouse_position):
                    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
                # If mouse is clicked on windowed button, game will set window to windowed
                if fullscreen_btn.checkForInput(mouse_position):
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Updating the display
        pygame.display.update()


def main_menu():
    # Setting the game to run in a loop
    while True:
        # Rendering the main menu background onto the screen
        screen.blit(BG, (0, 0))

        # Defining the mouse position
        mouse_position = pygame.mouse.get_pos()

        # Defining the main menu title along with positioning
        vibrant_title = get_font(120).render("VIBRANT", True, "#E2E958")
        vibrant_title_pos = vibrant_title.get_rect(center=(WIDTH - (WIDTH / 4.5), HEIGHT / 2.1))

        ventures_title = get_font(120).render("VENTURES", True, "#E2E958")
        ventures_title_pos = ventures_title.get_rect(center=(WIDTH - (WIDTH / 4), (HEIGHT / 2) + 120))

        # Rendering the title onto the screen
        screen.blit(vibrant_title, vibrant_title_pos)
        screen.blit(ventures_title, ventures_title_pos)

        # Defining navigation buttons for the main menu
        start_btn = Button(image=pygame.image.load("assets/Start Rect.png"), pos=(175, HEIGHT - 280),
                           text_input="Start", font=get_font(20), base_color="black", hovering_color="Gray")
        settings_btn = Button(image=pygame.image.load("assets/Settings Rect.png"), pos=(175, HEIGHT - 190),
                              text_input="Settings", font=get_font(20), base_color="black", hovering_color="Gray")
        exit_btn = Button(image=pygame.image.load("assets/Exit Rect.png"), pos=(175, HEIGHT - 100),
                          text_input="Exit", font=get_font(20), base_color="black", hovering_color="Gray")

        # Using for loop to change colour of buttons when hovered over
        for button in [start_btn, settings_btn, exit_btn]:
            button.changeColor(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            # If mouse is clicked on close window button, game will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If mouse is clicked on play button, game will start the character design
                if start_btn.checkForInput(mouse_position):
                    play()
                # If mouse is clicked on settings button, game will open settings
                if settings_btn.checkForInput(mouse_position):
                    settings()
                # If mouse is clicked on exit button, game will close
                if exit_btn.checkForInput(mouse_position):
                    pygame.quit()
                    sys.exit()

        # Updating the display
        pygame.display.update()


# calling the main menu function to start the game
main_menu()

import turtle
import random

# Game Constants
WIDTH = 600
HEIGHT = 600
DELAY = 100  # Milliseconds
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


# Default globals
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
food_pos = [0, 0]
score = 0
directions = list(offsets.keys())
snake_direction = random.choice(directions)
is_paused = False


# Direction functions
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def random_direction():
    global snake_direction
    snake_direction = random.choice(directions)


# Main game loop
def game_loop():
    global is_paused, snake
    if is_paused:
        screen.update()
        return

    # Clear the canvas
    stamper.clear()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check for collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body
        snake.append(new_head)

        # Check for food collision
        if not food_collision():
            snake.pop(0)

            # Draw snake's body
            for segment in snake[:-1]:
                stamper.goto(segment[0], segment[1])
                stamper.color("DarkGreen")
                stamper.stamp()

            # Draw snake's head (slightly larger than body) then reset stamp size
            head = snake[-1]
            stamper.goto(head[0], head[1])
            stamper.shapesize(1.3)
            stamper.stamp()
            stamper.shapesize(1)

        # Refresh screen
        screen.title(f"Snake Game ~ Score: {score}")
        screen.update()

        # Run the game at defined speed
        turtle.ontimer(game_loop, DELAY)


# Create a turtle for the menu display
menu = turtle.Turtle()
menu.hideturtle()
menu.penup()


# Handle Esc key press
def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        show_menu()
    else:
        resume_game()


# Show the pause menu
def show_menu():
    save_state()
    screen.tracer(1)  # Show the menu immediately
    menu.goto(0, 0)
    menu.color("white")
    menu.write("GAME PAUSED", align="center", font=("Arial", 24, "bold"))
    menu.goto(0, -40)
    menu.write("Press 'C' to continue", align="center", font=("Arial", 16, "normal"))
    menu.goto(0, -60)
    menu.write("Press 'R' to reset", align="center", font=("Arial", 16, "normal"))
    menu.goto(0, -80)
    menu.write("Press 'Q' to quit", align="center", font=("Arial", 16, "normal"))


# Hide the pause menu
def hide_menu():
    menu.clear()
    screen.tracer(0)


# Quit the game
def quit_game():
    global is_paused
    is_paused = False
    screen.bye()


# Detect food collision
def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


# Determine random placement of food
def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


# Get distance for food collision function
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Based on Pythagorean theorem
    return distance


# Save the snake's state
def save_state():
    global saved_snake, saved_food_pos, saved_score, saved_snake_direction, snake
    saved_snake = snake.copy()
    saved_food_pos = food_pos
    saved_score = score
    saved_snake_direction = snake_direction


# Resume the game
def resume_game():
    global snake, food_pos, score, snake_direction, is_paused
    hide_menu()
    snake = saved_snake.copy()
    food_pos = saved_food_pos
    score = saved_score
    snake_direction = saved_snake_direction
    is_paused = False
    game_loop()


# Reset the game, also called to initially start the game
def reset():
    global score, snake, food_pos, is_paused
    stamper.clear()
    hide_menu()
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    random_direction()
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    is_paused = False
    game_loop()


# Create a window, set dimensions, & disable auto-animation
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("gray")
screen.tracer(0)

# Register custom shape for the snake's head (triangle)
turtle.register_shape("snake_head", ((5, -5), (5, 5), (0, 10), (-5, 5), (-5, -5)))

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(toggle_pause, "Escape")  # Pause the game when Esc key is pressed
screen.onkey(resume_game, "c")  # Continue the game when 'C' is pressed
screen.onkey(reset, "r")  # Resume the game when 'R' is pressed
screen.onkey(quit_game, "q")  # Quit the game when 'Q' is pressed

# Define & create a snake (turtle)
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Define & create food
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(FOOD_SIZE / 20)
food.penup()


# Set animation in motion
reset()

# Finish turtle implementation
turtle.done()

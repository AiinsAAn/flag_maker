import turtle

# Function to draw the flag of the USA
def draw_usa_flag():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen mode
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the stripes
    for i in range(13):
        if i % 2 == 0:
            t.color("red")
        else:
            t.color("white")
        t.begin_fill()
        for _ in range(2):
            t.forward(400)
            t.right(90)
            t.forward(20)
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(-200, 100 - (i + 1) * 20)
        t.pendown()

    # Draw the blue rectangle
    t.penup()
    t.goto(-190, 100)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(180)
        t.right(90)
        t.forward(140)
        t.right(90)
    t.end_fill()

    # Draw the stars
    t.penup()
    t.goto(-180, 80)
    t.color("white")
    for row in range(5):
        for col in range(6):
            t.goto(-180 + col * 30, 80 - row * 25)
            t.begin_fill()
            for _ in range(5):
                t.forward(10)
                t.right(144)
            t.end_fill()
    t.hideturtle()

# Function to draw the flag of France
def draw_france_flag():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen mode
    screen.bgcolor("Black")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the blue stripe
    t.color("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    # Draw the white stripe
    t.penup()
    t.goto(-67, 100)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    # Draw the red stripe
    t.penup()
    t.goto(66, 100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    t.hideturtle()

# Function to draw the flag of India
def draw_india_flag():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen mode
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the saffron stripe
    t.color("#FF9933")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()

    # Draw the white stripe
    t.penup()
    t.goto(-200, 34)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()

    # Draw the green stripe
    t.penup()
    t.goto(-200, -32)
    t.pendown()
    t.color("#138808")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()

    # Draw the Ashoka Chakra
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("navy")
    t.circle(20)
    for i in range(24):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.setheading(i * 15)
        t.forward(20)
        t.pendown()
        t.forward( 5)
    t.hideturtle()

# Function to draw the flag of Germany
def draw_germany_flag():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen mode
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the black stripe
    t.color("black")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()

    # Draw the red stripe
    t.penup()
    t.goto(-200, 34)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()

    # Draw the yellow stripe
    t.penup()
    t.goto(-200, -32)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(66)
        t.right(90)
    t.end_fill()
    t.hideturtle()

# Function to draw the flag of Italy
def draw_italy_flag():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the green stripe
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    # Draw the white stripe
    t.penup()
    t.goto(-67, 100)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    # Draw the red stripe
    t.penup()
    t.goto(66, 100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(133)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    t.hideturtle()

# Main function to take user input and draw the corresponding flag
def main():
    country = input("Enter the country name (USA, France, India, Germany, Italy): ").strip().lower()
    if country == "usa":
        draw_usa_flag()
    elif country == "france":
        draw_france_flag()
    elif country == "india":
        draw_india_flag()
    elif country == "germany":
        draw_germany_flag()
    elif country == "italy":
        draw_italy_flag()
    else:
        print("Sorry, flag design for this country is not available.")
    turtle.done()

if __name__ == "__main__":
    main()
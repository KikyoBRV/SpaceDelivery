import math
import turtle
import time
import random

# Screen width & height
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

# Create Game Screen
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Delivery! by @KikyoBRV")
wn.bgcolor("black")
wn.tracer(0)

# Pen object
pen01 = turtle.Turtle()
pen01.speed(0)
pen01.shape("square")
pen01.color("white")
pen01.penup()
pen01.hideturtle()

# Draw border
my_pen = turtle.Turtle()

# Draw Parcel delivery point
parcel_point_pen = turtle.Turtle()

# Draw Arrow Sign
arrow = turtle.Turtle()

# Write context at Parcel delivery point
text = turtle.Turtle()

# Create pen object to draw (almost) everything in this game
pen_main = turtle.Turtle()

# Create information board
info = turtle.Turtle()

# Write High score and the owner of this High score
pen_high_score = turtle.Turtle()

# Create pen object to draw score
pen_score = turtle.Turtle()

# Create pen object to draw parcels collected
pen_parcel = turtle.Turtle()

# Create pen object to draw spaceship's speed
pen_speed = turtle.Turtle()


class CharacterPen:
    def __init__(self, color="white", scale=1.0):
        self.color = color
        self.scale = scale
        self.characters = {}
        self.characters["2"] = ((-5, 10), (5, 10), (5, 0), (-5, 0), (-5, -10),
                                (5, -10))
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0),
                                (5, -10))
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0, 0), (0, -10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10),
                                (-5, 10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0),
                                (0, 0))
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10))
        self.characters["A"] = ((-5, -10), (0, 10), (5, -10), (2.5, 0),
                                (-2.5, 0))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, -10), (3, 10),
                                (5, -10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, -10), (5, -10),
                                (-5, -10), (-5, 0), (5, 0))
        self.characters["H"] = ((-5, -10), (-5, 10), (-5, 0), (5, 0), (5, 10),
                                (5, -10))
        self.characters["B"] = ((-5, 10), (-5, -10), (2, -10), (4, -7),
                                (4, -3), (2, 0), (-5, 0), (2, 0), (4, 3),
                                (4, 7), (2, 10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 2), (-5, 2))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 2), (-5, 2),
                                (5, -10))
        self.characters["S"] = ((5, 7), (0, 10), (-5, 7), (5, -7), (0, -10),
                                (-5, -7))
        self.characters["T"] = ((0, -10), (0, 10), (-5, 10), (5, 10))
        self.characters["C"] = ((5, 8), (5, 10), (-5, 10), (-5, -10), (5, -10),
                                (5, -8))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, -10), (-5, 0), (5, 0))
        self.characters["D"] = ((-5, 10), (-5, -10), (2, -10), (5, -5), (5, 5),
                                (2, 10), (-5, 10))
        self.characters["I"] = ((0, 10), (5, 10), (-5, 10), (0, 10), (0, -10),
                                (5, -10), (-5, -10))
        self.characters["V"] = ((0, -10), (5, 10), (0, -10), (-5, 10))
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 10), (3, -10),
                                (5, 10))

    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)

        # Center text
        x -= 15 * self.scale * (len(str)-1 / 2)
        for character in str:
            self.draw_characters(pen, character, x, y)
            x += 15 * self.scale

    def draw_characters(self, pen, character, x, y):
        scale = self.scale

        character = character.upper()

        # Check if the character is in the dictionary
        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()


class Game:
    # Constructor
    def __init__(self, player):
        self.player = player
        self.current_parcel = None
        self.high_score = ["", 0]
        self.player_name = ""
        self.welcome_screen()

    def is_collision(self):
        return self.player.is_collision(self.current_parcel)

    def welcome_screen(self):
        my_pen.clear()
        parcel_point_pen.clear()
        arrow.clear()
        text.clear()
        pen_main.clear()
        info.clear()
        pen_high_score.clear()
        pen_score.clear()
        pen_parcel.clear()
        pen_speed.clear()
        character_pen = CharacterPen("white", 1.0)
        character_pen2 = CharacterPen("lightblue", 5.0)
        character_pen3 = CharacterPen("red", 2.0)
        character_pen2.draw_string(pen01, "SPACE DELIVERY", 530, 200)
        character_pen.draw_string(pen01, "GAME BY KYO SKE2O", 120, 100)
        character_pen.draw_string(pen01, "PRESS W TO GO UP", 110, 0)
        character_pen.draw_string(pen01, "PRESS A TO TURN LEFT", 140, -50)
        character_pen.draw_string(pen01, "PRESS S TO GO DOWN", 130, -100)
        character_pen.draw_string(pen01, "PRESS D TO TURN RIGHT", 150, -150)
        character_pen3.draw_string(pen01, "PRESS H TO START", 250, -250)
        wn.update()
        print("Space Delivery! By KikyoBRV")
        self.player_name = wn.textinput("Pls, Enter your name", "Name: ")
        while self.player_name == "":
            self.player_name = wn.textinput("Pls, Enter your name", "Name: ")
        wn.listen()
        wn.onkeypress(self.start_game, "h")
        while self.player_name != "":
            wn.update()

    def start_game(self):
        # Clear Screen
        pen01.clear()

        # Get High score player's name
        with open('player_score.txt') as f:
            lines = f.read().splitlines()
        tables = [x.split(",") for x in lines if x != ""]
        for check in tables:
            if int(check[1]) > int(self.high_score[1]):
                self.high_score = [check[0], check[1]]

        # Draw border
        my_pen.color("white")
        my_pen.penup()
        my_pen.setposition(-515, -315)
        my_pen.pendown()
        my_pen.pensize(3)
        my_pen.speed(50)
        my_pen.forward(630)
        my_pen.left(90)
        my_pen.forward(305)
        my_pen.penup()
        my_pen.forward(20)
        my_pen.pendown()
        my_pen.forward(305)
        my_pen.left(90)
        for draw in range(2):
            my_pen.forward(630)
            my_pen.left(90)
        my_pen.hideturtle()

        # Draw Parcel delivery point
        parcel_point_pen.color("light green")
        parcel_point_pen.pensize(3)
        parcel_point_pen.speed(50)
        parcel_point_pen.penup()
        parcel_point_pen.setposition(120, -315)
        parcel_point_pen.pendown()
        parcel_point_pen.fillcolor("light green")
        parcel_point_pen.begin_fill()
        for pen in range(4):
            if pen % 2 == 0:
                parcel_point_pen.forward(100)
                parcel_point_pen.left(90)
            else:
                parcel_point_pen.forward(630)
                parcel_point_pen.left(90)
        parcel_point_pen.end_fill()
        parcel_point_pen.hideturtle()

        # Draw Arrow Sign
        arrow.color("white")
        arrow.pensize(3)
        arrow.speed(50)
        arrow.penup()
        arrow.setposition(50, 0)
        arrow.pendown()
        arrow.forward(50)
        arrow.left(135)
        arrow.forward(25)
        arrow.left(180)
        arrow.forward(25)
        arrow.right(90)
        arrow.forward(25)
        arrow.left(180)
        arrow.right(45)
        arrow.hideturtle()

        # Write context at Parcel delivery point
        text.color("dark green")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(173, 40)
        text.pendown()
        text.write("Parcel", align="center",
                   font=("Courier", 15, "italic"))
        text.penup()
        text.setposition(173, 10)
        text.pendown()
        text.write("delivery", align="center",
                   font=("Courier", 15, "italic"))
        text.penup()
        text.setposition(173, -20)
        text.pendown()
        text.write("point", align="center",
                   font=("Courier", 15, "italic"))
        text.hideturtle()

        # Create pen object to draw (almost) everything in this game
        pen_main.speed(0)
        pen_main.shape("square")
        pen_main.color("white")
        pen_main.penup()
        pen_main.hideturtle()

        # Create information board
        info.color("white")
        info.pensize(3)
        info.speed(50)
        info.penup()
        info.setposition(295, -320)
        info.pendown()
        info.begin_fill()
        for draw in range(4):
            if draw % 2 == 0:
                info.forward(310)
                info.left(90)
            else:
                info.forward(640)
                info.left(90)
        info.end_fill()
        info.color("#222255")
        info.pensize(3)
        info.speed(50)
        info.penup()
        info.setposition(300, -315)
        info.pendown()
        info.begin_fill()
        for draw in range(4):
            if draw % 2 == 0:
                info.forward(300)
                info.left(90)
            else:
                info.forward(630)
                info.left(90)
        info.end_fill()
        info.hideturtle()

        # Write Game's name
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(450, 250)
        text.pendown()
        text.write("Space Delivery", align="center",
                   font=("Courier", 25, "italic"))
        text.penup()
        text.setposition(450, 220)
        text.pendown()
        text.write("By KikyoBRV", align="center",
                   font=("Courier", 12, "italic"))
        text.hideturtle()

        # Write High score and the owner of this High score
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(390, 140)
        text.pendown()
        text.write("High Score:", align="center",
                   font=("Courier", 18, "italic"))
        text.penup()
        text.hideturtle()
        pen_high_score.color("white")
        pen_high_score.shapesize()
        pen_high_score.speed(50)
        pen_high_score.penup()
        pen_high_score.setposition(445, 100)
        pen_high_score.pendown()
        pen_high_score.write(f"{self.high_score[1]} By {self.high_score[0]}",
                             align="center", font=("Courier", 15, "normal"))
        pen_high_score.penup()
        pen_high_score.hideturtle()

        # Write score text
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(390, 50)
        text.pendown()
        text.write("Your Score:", align="center",
                   font=("Courier", 18, "italic"))
        text.penup()
        text.hideturtle()

        # Write number of parcel in play text
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(440, -40)
        text.pendown()
        text.write("Parcels collected:", align="center",
                   font=("Courier", 18, "italic"))
        text.penup()
        text.hideturtle()

        # Write spaceship's speed
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(440, -120)
        text.pendown()
        text.write("Spaceship's speed:", align="center",
                   font=("Courier", 18, "italic"))
        text.penup()
        text.hideturtle()

        # Write caution of game challenge
        text.color("Red")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(15, -360)
        text.pendown()
        text.write("Caution! Every times you go to parcel delivery point, "
                   "your spaceship's speed is increase.",
                   align="center", font=("Courier", 15, "italic"))
        text.penup()
        text.setposition(15, -390)
        text.pendown()
        text.write("And remember that don't crash spaceship into itself!!",
                   align="center", font=("Courier", 15, "italic"))
        text.penup()
        text.hideturtle()

        # Write bonus score info
        text.color("white")
        text.shapesize()
        text.speed(50)
        text.penup()
        text.setposition(430, -210)
        text.pendown()
        text.write("Bonus score info:", align="center",
                   font=("Courier", 18, "italic"))
        text.penup()
        text.setposition(430, -240)
        text.pendown()
        text.write("10 parcels collected = +10 scores", align="center",
                   font=("Courier", 9, "italic"))
        text.penup()
        text.setposition(433, -270)
        text.pendown()
        text.write("50 parcels collected = +100 scores", align="center",
                   font=("Courier", 9, "italic"))
        text.penup()
        text.setposition(433, -300)
        text.pendown()
        text.write("100 parcels collected = +300 scores", align="center",
                   font=("Courier", 9, "italic"))
        text.penup()
        text.hideturtle()

        # Create pen object to draw score
        pen_score.speed(0)
        pen_score.shape("square")
        pen_score.color("white")
        pen_score.penup()
        pen_score.hideturtle()
        pen_score.goto(445, 10)
        pen_score.write(f"0 By {self.player_name}", align="center",
                        font=("Courier", 15, "normal"))

        # Create pen object to draw parcels collected
        pen_parcel.speed(0)
        pen_parcel.shape("square")
        pen_parcel.color("white")
        pen_parcel.penup()
        pen_parcel.hideturtle()
        pen_parcel.goto(445, -80)
        pen_parcel.write("0", align="center",
                         font=("Courier", 15, "normal"))

        # Create pen object to draw spaceship's speed
        pen_speed.speed(0)
        pen_speed.shape("square")
        pen_speed.color("white")
        pen_speed.penup()
        pen_speed.hideturtle()
        pen_speed.goto(440, -150)
        pen_speed.write("Speed +0", align="center",
                        font=("Courier", 15, "italic"))

        # Score and status of player
        total_score = 0
        bonus_score = 0
        parcel_score = 0
        border_crash = 0
        self_destroy = 0
        player_speed = 0

        # Delay
        delay = 0.07

        # Key_board bindings
        wn.listen()
        wn.onkeypress(player.go_up, "w")
        wn.onkeypress(player.go_down, "s")
        wn.onkeypress(player.go_left, "a")
        wn.onkeypress(player.go_right, "d")

        # Create first parcel
        # This x and y is just define for start loop
        x = 0
        y = 0
        while x == 0 and y == 0:
            x = random.sample(range(int(-600/2)-200, int(600/2)-200, 20), 1)
            y = random.sample(range(int(-600/2), int(600/2), 20), 1)
        self.current_parcel = Parcel(x[0], y[0], "square", "#3366CC")

        while True:
            # Clear screen
            pen_main.clear()

            # Update player data
            last_player_x = player.x
            last_player_y = player.y
            player.update()

            # Check collision between player and parcel in self.parcels
            if player.player_and_parcel_collision():
                with open("player_score.txt", "a") as f:
                    f.write('\n')
                    f.write(f"{self.player_name}, {total_score}")
                time.sleep(1)
                self_destroy = 1
                total_score = 0
                delay = 0.07
                player_speed = 0
                player.parcels.clear()
                player.x = -200
                player.y = 0
                player.heading = 90
                player.direction = "stop"
                self.welcome_screen()

            # Update player bonus score
            if player.x == 120 and player.y == 0:
                if delay >= 0.03:
                    delay -= 0.005
                    player_speed += 0.5
                if len(player.parcels) // 100 != 0:
                    total_score += 300
                elif len(player.parcels) // 50 != 0:
                    total_score += 100
                elif len(player.parcels) // 10 != 0:
                    total_score += 10
                bonus_score = 1
                player.parcels.clear()
                player.x = -200
                player.y = 0
                player.heading = 90
                player.direction = "stop"

            # Check collision between player and border
            if player.position != (120, 0):
                if player.x >= 125 or player.x <= -520:
                    with open("player_score.txt", "a") as f:
                        f.write('\n')
                        f.write(f"{self.player_name}, {total_score}")
                    border_crash = 1
                    total_score = 0
                    delay = 0.07
                    player_speed = 0
                    player.parcels.clear()
                    player.x = -200
                    player.y = 0
                    player.heading = 90
                    player.direction = "stop"
                    self.welcome_screen()

                elif player.y >= 320 or player.y <= -320:
                    with open("player_score.txt", "a") as f:
                        f.write('\n')
                        f.write(f"{self.player_name}, {total_score}")
                    border_crash = 1
                    total_score = 0
                    delay = 0.07
                    player_speed = 0
                    player.parcels.clear()
                    player.x = -200
                    player.y = 0
                    player.heading = 90
                    player.direction = "stop"
                    self.welcome_screen()

            # Check collision
            # If player collect parcel, this condition will activate
            if player.is_collision(self.current_parcel):
                self.current_parcel.state = "collected"
                self.current_parcel.color = "#FFCCCC"
                self.player.parcels.append(self.current_parcel)
                parcel_score = 1
                total_score += 1
                state = "work"
                while True:
                    x = random.sample(range(int(-600 / 2)-200,
                                            int(600 / 2)-200, 20), 1)
                    y = random.sample(range(int(-600 / 2),
                                            int(600 / 2), 20), 1)
                    for parcel in player.parcels:
                        if x[0] == parcel.x and y[0] == parcel.y:
                            break
                        elif x[0] == player.x and y[0] == player.y:
                            break
                        if parcel == player.parcels[-1]:
                            state = "stop"
                    if state == "stop":
                        break
                self.current_parcel = Parcel(x[0], y[0], "square", "#3366CC")

            # Move the other parcel to follow player
            for index in range(len(player.parcels)-1, 0, -1):
                x = player.parcels[index-1].x
                y = player.parcels[index-1].y
                player.parcels[index].update(x, y)

            # Move the first parcel to follow player
            if len(player.parcels) > 0:
                x = last_player_x
                y = last_player_y
                player.parcels[0].update(x, y)

            # Render
            player.render(pen_main)
            self.current_parcel.render(pen_main)
            time.sleep(delay)
            if bonus_score != 0 or parcel_score != 0 or border_crash != 0 or \
                    self_destroy != 0:
                if total_score > int(self.high_score[1]):
                    pen_high_score.clear()
                    pen_high_score.write(
                        f"{total_score} By {self.player_name}",
                        align="center", font=("Courier", 15, "normal"))

                pen_score.clear()
                pen_score.write(f"{total_score} By {self.player_name}",
                                align="center", font=("Courier", 15, "normal"))
                pen_parcel.clear()
                pen_parcel.write(f"{len(player.parcels)}", align="center",
                                 font=("Courier", 15, "normal"))
                pen_speed.clear()
                pen_speed.write(f"Speed +{player_speed}", align="center",
                                font=("Courier", 15, "italic"))
                bonus_score = 0
                parcel_score = 0
                border_crash = 0
                self_destroy = 0

            wn.update()


class Player:
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.shape = shape
        self.color = color
        self.width = 20
        self.height = 20
        self.heading = 90
        self.direction = "stop"
        self.parcels = []

    def is_collision(self, other):
        distance = math.sqrt(math.pow((self.x - other.x), 2))\
                   + math.sqrt(math.pow((self.y - other.y), 2))
        if distance < self.width:
            return True
        else:
            return False

    def player_and_parcel_collision(self):
        for parcel in self.parcels:
            distance = math.sqrt(math.pow((self.x - parcel.x), 2)) \
                       + math.sqrt(math.pow((self.y - parcel.y), 2))
            if distance < self.width:
                return True
        return False

    def go_up(self):
        if self.direction != "down" or len(self.parcels) == 0:
            self.direction = "up"

    def go_down(self):
        if self.direction != "up" or len(self.parcels) == 0:
            self.direction = "down"

    def go_left(self):
        if self.direction != "right" or len(self.parcels) == 0:
            self.direction = "left"

    def go_right(self):
        if self.direction != "left" or len(self.parcels) == 0:
            self.direction = "right"

    def update(self):
        if self.direction == "up":
            self.heading = 90
            self.y += 20
        if self.direction == "down":
            self.heading = 270
            self.y -= 20
        if self.direction == "left":
            self.heading = 180
            self.x -= 20
        if self.direction == "right":
            self.heading = 0
            self.x += 20

    def render(self, pen):
        pen.shapesize(1.0, 1.5)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0, 1.0, None)

        # Render each parcel in self.parcels
        for parcel in self.parcels:
            parcel.render(pen)


class Parcel:
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.width = 20
        self.height = 20

    def update(self, x, y):
        self.x = x
        self.y = y

    def render(self, pen):
        pen.shapesize(1.0, 1.0)
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        pen.shapesize(1.0, 1.0, None)

player = Player(-200, 0, "triangle", "#CC0033")
game = Game(player)

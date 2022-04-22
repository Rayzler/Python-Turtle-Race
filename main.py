import turtle
import random

screen = turtle.Screen()
screen.bgcolor("gray")


def initialize_turtle(player, color, pos_x, pos_y):
    player.hideturtle()
    player.speed(10)
    player.shape("turtle")
    player.shapesize(2, 2)
    player.color(color, color)
    player.penup()
    player.goto(pos_x, pos_y)
    player.pensize(3)


def draw_goal(player, radius):
    player.fd(500)
    player.rt(90)
    player.fd(radius)
    player.lt(90)
    player.pendown()
    player.circle(radius)
    player.penup()
    player.lt(90)
    player.fd(radius)
    player.rt(90)
    player.bk(500)
    player.pendown()
    player.speed(1)
    player.showturtle()


def throw_dice():
    return random.randint(1, 6)


winner_exists = False

player_one = turtle.Turtle()
initialize_turtle(player_one, "red", -250, 125)
draw_goal(player_one, 40)

player_two = turtle.Turtle()
initialize_turtle(player_two, "yellow", -250, -125)
draw_goal(player_two, 40)

while not winner_exists:
    move = throw_dice() * 25
    if (player_one.xcor() + move) >= 210:
        player_one.setx(250)
    else:
        player_one.fd(move)
    print(f"Player 1: dice = {int(move / 25)}, moves = {move}")

    move = throw_dice() * 25
    if (player_two.xcor() + move) >= 210:
        player_two.setx(250)
    else:
        player_two.fd(move)
    print(f"Player 2: dice = {int(move / 25)}, moves = {move}")

    if player_one.xcor() >= 210:
        print("Player one wins!")
        winner_exists = True
    elif player_two.xcor() >= 210:
        print("Player two wins!")
        winner_exists = True

turtle.done()

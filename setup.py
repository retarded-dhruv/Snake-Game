import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0

#Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
#the width the hight can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("pink")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['sqaure', 'traingle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("sqaure")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center", font=("calender",24, "bold"))

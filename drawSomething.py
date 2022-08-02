import turtle

window = turtle.Screen()
window.title("Draw Something")
window.setup(width=750, height=750)

pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.color("black")

border = turtle.Turtle()
border.speed(0)
border.width(2)
border.penup()
border.color("grey")
border.goto(-390, -325)
border.pendown()
border.goto(390,-325)


clearBtn = turtle.Turtle()
clearBtn.speed(0)
clearBtn.penup()
clearBtn.goto(-350, -345)
clearBtn.shape("square")
clearBtn.color("black")

colour = turtle.Turtle()
colour.speed(0)
colour.penup()
colour.hideturtle()
colour.goto(-330, -345)
colour.write("Colours:", font=("Calibri", 10, "bold"))

blackBtn = turtle.Turtle()
blackBtn.speed(0)
blackBtn.shape("circle")
blackBtn.color("black")
blackBtn.penup()
blackBtn.goto(-275, -345)

orangeBtn = turtle.Turtle()
orangeBtn.speed(0)
orangeBtn.shape("circle")
orangeBtn.color("orange")
orangeBtn.penup()
orangeBtn.goto(-245, -345)

greenBtn = turtle.Turtle()
greenBtn.speed(0)
greenBtn.shape("circle")
greenBtn.color("green")
greenBtn.penup()
greenBtn.goto(-215, -345)

blueBtn = turtle.Turtle()
blueBtn.speed(0)
blueBtn.shape("circle")
blueBtn.color("blue")
blueBtn.penup()
blueBtn.goto(-185, -345)

def up():
    pen.setheading(90)
    pen.forward(50)
    pen.xcor()

def down():
    pen.setheading(270)
    pen.forward(50)

def left():
    pen.setheading(180)
    pen.forward(50)

def right():
    pen.setheading(0)
    pen.forward(50)

def clearDrawing(x,y):
    pen.penup()
    pen.clear()
    pen.goto(0,0)
    pen.pendown()

def changeToBlack(x,y):
    xCor = pen.xcor()
    yCor = pen.ycor()
    pen.color("black")
    pen.penup()
    pen.goto(xCor,yCor)
    pen.down()

def changeToOrange(x,y):
    xCor = pen.xcor()
    yCor = pen.ycor()
    pen.color("orange")
    pen.penup()
    pen.goto(xCor,yCor)
    pen.down()

def changeToGreen(x,y):
    xCor = pen.xcor()
    yCor = pen.ycor()
    pen.color("green")
    pen.penup()
    pen.goto(xCor,yCor)
    pen.down()

def changeToBlue(x,y):
    xCor = pen.xcor()
    yCor = pen.ycor()
    pen.color("blue")
    pen.penup()
    pen.goto(xCor,yCor)
    pen.down()

def penUpandBackDown(x,y):
    if y > -325:
        pen.penup()
        pen.goto(x,y)
        pen.pendown()
    
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
clearBtn.onclick(clearDrawing)
blackBtn.onclick(changeToBlack)
orangeBtn.onclick(changeToOrange)
greenBtn.onclick(changeToGreen)
blueBtn.onclick(changeToBlue)
window.onclick(penUpandBackDown)


window.mainloop()

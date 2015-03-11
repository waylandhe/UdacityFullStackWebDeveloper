import turtle

def drawSquare(someTurtle):
	linesToBeDrawn = 4
	linesDrawn = 0

	while linesDrawn < linesToBeDrawn:
		someTurtle.forward(100)
		someTurtle.right(90)
		linesDrawn += 1

def drawTriangle(someTurtle):
	linesToBeDrawn = 3
	linesDrawn = 0

	while linesDrawn < linesToBeDrawn:
		someTurtle.forward(100)
		someTurtle.right(120)
		linesDrawn += 1

def drawCircle(someTurtle):

	someTurtle.circle(100)

#Initialize the window
window = turtle.Screen()
window.bgcolor("red")

#Create brad and make him draw a square
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(2)
drawSquare(brad)

#Create angie and make her draw a circle
angie = turtle.Turtle()
angie.shape("turtle")
angie.color("blue")
angie.speed(2)
drawCircle(angie)

#Create bob and make him draw a triangle
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")
bob.speed(2)
drawTriangle(bob)

window.exitonclick()
import turtle

def draw_art():
  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(10)
  for i in range(0,36):
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.right(10)
  window.exitonclick()

draw_art()
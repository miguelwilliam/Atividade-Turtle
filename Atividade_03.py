"""
Exercícios

1) Mude/defina a forma da tartaruga - FEITO
2) Mude a ordem das cores - FEITO
3) Mude a largura da linha - FEITO
4) Faça a tartaruga desenhar dois quadrados - FEITO
"""

import turtle

turtle = turtle.Turtle()
turtle.shape('square')
turtle.pensize(7)

for i in range(2):
    for color in ['pink', 'black', 'red', 'blue']:
        turtle.color(color)
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
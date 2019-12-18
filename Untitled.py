import turtle

smiles = turtle.Turtle()

smiles.penup()
smiles.goto(-105,155)
smiles.pendown()
smiles.goto(-45,115)

smiles.penup()
smiles.goto(-75,75)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(105,155)
smiles.pendown()
smiles.goto(45,115)

smiles.penup()
smiles.goto(75,75)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(0,25)
smiles.pendown()
smiles.circle(-100,80)

smiles.penup()
smiles.setheading(180)
smiles.goto(0,25)
smiles.pendown()
smiles.circle(100,80)

turtle.done()

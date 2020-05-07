import turtle
print((('---'*4)),'PROGRAMA TARTARUGA',('---'*4))
corfundo = str(input('Diga a cor do fundo: ')).lower()
caneta = int(input('Diga a grossura da caneta(1 a 50): '))
corcaneta = str(input('Diga a cor da caneta: '))
bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor(corfundo)
bob.pensize(caneta)
bob.pencolor(corcaneta)
for c in range(1,7):
    bob.forward(100)
    bob.left(60)
wn.exitonclick()
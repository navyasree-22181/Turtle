from turtle import *
colors=['blue','red','orange','green','yellow']
for angle in range(0,360,15):
    pencolor(colors[angle%5])
    setheading(angle)
    forward(100)
    write(str(angle)+ '0')
    backward(100)





from turtle import *
pencolor('blue)
for i in range(15):
         forward(100)
         left(90)
         forward(10)
         left(90)
         forward(100)
         right(90)
         forward(10)
         right(90)
pencolor('red')


         

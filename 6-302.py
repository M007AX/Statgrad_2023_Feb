from turtle import *
speed(0) #самая быстрая {'fastest':0, 'fast':10, 'normal':6, 'slow':3, 'slowest':1 } см. исходную библиотеку
for i in range(3):
    forward(7*40)
    right(90)
forward(8*40)
for i in range(3):
    left(90)
    forward(5*40)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*40, y*40)
        dot(4, 'red')

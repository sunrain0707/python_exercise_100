#57.画直线

import turtle

def drawline(n):
    t=turtle.Pen()
    t.color(0.2,0.5,0.8)  #设置颜色，在0--1之间
    t.begin_fill()
    for i in range(n):
        t.forward(50)
        t.left(360/n)
    t.end_fill()   #结束填充颜色

drawline(4)

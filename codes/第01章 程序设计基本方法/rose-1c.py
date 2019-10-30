#turtle绘制玫瑰

import turtle
from turtle import *
#global pen and speed
pencolor("black")
fillcolor("red")
speed(50)
s=0.15
#init poistion
penup()
goto(0,600*s)
pendown()

begin_fill()
circle(200*s,30)
for i in range(60):
    lt(1)
    circle(50*s,1)
circle(200*s,30)
for i in range(4):
    lt(1)
    circle(100*s,1)
circle(200*s,50)
for i in range(50):
    lt(1)
    circle(50*s,1)
circle(350*s,65)
for i in range(40):
    lt(1)
    circle(70*s,1)
circle(150*s,50)
for i in range(20):
    rt(1)
    circle(50*s,1)
circle(400*s,60)
for i in range(18):
    lt(1)
    circle(50*s,1)

fd(250*s)
rt(150)
circle(-500*s,12)
lt(140)
circle(550*s,110)
lt(27)
circle(650*s,100)
lt(130)
circle(-300*s,20)
rt(123)
circle(220*s,57)
end_fill()

lt(120)
fd(280*s)
lt(115)
circle(300*s,33)
lt(180)
circle(-300*s,33)
for i in range(70):
    rt(1)
    circle(225*s,1)
circle(350*s,104)
lt(90)
circle(200*s,105)
circle(-500*s,63)

penup()
goto(170*s,-330*s)
pendown()
lt(160)
for i in range(20):
    lt(1)
    circle(2500*s,1)
for i in range(220):
    rt(1)
    circle(250*s,1)
    
fillcolor('green')
penup()
goto(670*s,-480*s)
pendown()
rt(140)
begin_fill()
circle(300*s,120)
lt(60)
circle(300*s,120)
end_fill()
penup()
goto(180*s,-850*s)
pendown()
rt(85)
circle(600*s,40)

penup()
goto(-150*s,-1300*s)
pendown()

begin_fill()
rt(120)
circle(300*s,115)
lt(75)
circle(300*s,100)
end_fill()
penup()
goto(430*s,-1370*s)
pendown()
rt(30)
circle(-600*s,35)
done()

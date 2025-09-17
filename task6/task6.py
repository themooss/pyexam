from turtle import *

def task6_1():
    f = 5
    for _ in range(5):
        forward(40*f); right(90); fd(46*f); rt(90)
    up()
    fd(19*f); rt(90); fd(19); rt(90)
    down()
    for _ in range(5):
            fd(37); rt(90); fd(19); rt(90)

    up()
    for x in range(0, 5000, 50):
        for y in range(0, 5000, 50):
            goto(x, y)
            dot(3, 'red')
            up()

def task6_19238_2():
    l = 10
    left(90)
    speed(50000)

    for _ in range(8):
          fd(16*l); rt(90); fd(22*l); rt(90)
    up()

    fd(5*l); rt(90); fd(5*l); lt(90)

    down()

    for _ in range(8):
         fd(52*l); rt(90); fd(77*l); rt(90)
    up()
    for x in range(0, 40):
         for y in range(0, 17):
              goto(x*l, y * l)
              dot(3, 'red')
task6_19238_2()
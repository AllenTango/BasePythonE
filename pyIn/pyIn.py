# py => 可执行文件

import turtle as t

def drawGap():
    t.pu()
    t.fd(5)
def drawLine(draw):
    drawGap()
    t.pd() if draw else t.pu()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8, 9] else drawLine(False)
    # drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180)
    t.pu()
    t.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def main():
    t.setup(800, 350, 200, 200)
    t.pu()
    t.fd(-300)
    t.pensize(5)
    drawDate('20181010')
    t.hideturtle()
    t.done()

main()
# 绘制六边形

import turtle as t
import random

# 绘制单个六边形
def drawHexagon():
    t.pensize(10)
    for i in range(6):
        t.pencolor(random.choice(['blue', 'green', 'red', 'magenta', 'gold', 'pink', 'tomato', 'purple']))
        t.fd(50)
        t.right(60)


def main():
    for i in range(6):
        drawHexagon()
        t.right(60)
    t.done()

main()
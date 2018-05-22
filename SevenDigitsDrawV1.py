# 七段数码管绘制 基本思路
# 1. 绘制单个数字对应的数码管
# 2. 获得一串数字，绘制对应的数码管
# 3. 获得当前系统时间，绘制对应的数码管

import turtle as t
import time

# 绘制数码管间隔
def drawGap():
    t.pu()
    t.fd(4)

# 绘制单段数码管
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)


# 根据数字绘制七段数码管
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180)
    t.penup()  # 为绘制后续数字确定位置
    t.fd(20)  # 为绘制后续数字确定位置
    # t.done()   这不是随便用的，需要在主函数调用时，最好不要出现哦

# 获取要输出的数字，通过eval()函数将数字转变为整数
def drawDate(date):
    # for i in date:
    #     drawDigit(eval(i))
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write('年', font=("Arial", 24, "normal"))
            t.pencolor("green")
            t.fd(35)
        elif i == '=':
            t.write('月', font=("Arial", 24, "normal"))
            t.pencolor("blue")
            t.fd(35)
        elif i == '+':
            t.write('日', font=("Arial", 24, "normal"))
        else:
            drawDigit(eval(i))

# 组合模块
def main():
    t.setup(800, 400, 200, 200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    # drawDate('20181010')
    # 查询系统时间，并格式化传入drawDate()函数
    drawDate(time.strftime('%Y-%m-%d+', time.gmtime()))
    t.hideturtle()
    t.done()


main()
# 简单用户输入，公式转换之温度转换

TempStr = input("请输入带有符号的温度值[如23C]：")

while True:
    if TempStr[-1] in ['f', 'F']:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        print("转换后的温度是：{:.2f}C".format(C))
        break
    elif TempStr[-1] in ['c', 'C']:
        F = 1.8 * eval(TempStr[0:-1]) + 32
        print("转换后的温度是：{:.2f}F".format(F))
        break
    else:
        print("输入格式有误，请重新输入")
        TempStr = input("请输入带有符号的温度值[如23C]：")
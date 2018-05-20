# 天天向上的力量第二版

dayFactor = 0.01
dayup = pow(1 + dayFactor, 365)
daydown = pow(1 - dayFactor, 365)
print("天天向上：{:.2f}， 天天向下：{:.2f}".format(dayup, daydown))
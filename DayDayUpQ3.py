# 天天向上的力量第三版之工作日的力量

dayup = 1.0
dayfactor = 0.01

for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup *= 1 + dayfactor

print("工作日的力量：{:.2f}".format(dayup))
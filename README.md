# Python 程序设计

## 程序的基本编写方法(IPO)

- I : Input 输入，程序的输入
- P : Process 处理，程序的主要逻辑
- O : Output 输出，程序的输出

## 保留字

and|elif|import|in|global
---|---|---|---|---|
as|else|raise|return|nonlocal
assert|except|is|try|True
break|finally|lamba|while|False
class|for|not|with|None
continue|from|or|yield|
def|if|pass|del|

<!--  如何 隐藏部分文字呢2018.520-->
## 数据类型：字符串、整数、浮点数、列表

- 字符串的序号

-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1
---|---|---|---|---|---|---|---|---|---|---|---
请|输|入|带|有|符|号|的|温|度|值|：
0|1|2|3|4|5|6|7|8|9|10|11

- 索引    <字符串>[M]    返回特定位置单个字符
- 切片    <字符串>[M:N]  返回由M到N前的一段字符
- 高级切片 <字符串>[M:N:K] 以步长K对字符串切片

评估函数 eval(<字符串或字符串变量>)
`eval('1')   =>  1`


## turtle 库

设置窗口大小，起始位置

`turtle.setup(width, height, startx, starty)`

绝对坐标体系(X,Y)
`turtle.goto(x, y)`

turtle 空间坐标体系
```python
turtle.fd(d)
turtle.bk(d)
turtle.circle(r,extent)
```
turtle 角度坐标体系 
```python
turtle.seth(angle) # 绝对角度
turtle.left(angle)  # 海龟角度
turtle.right(angle)
```

- seth()    改变海龟行进方向
- angle     为绝对度数
- seth()    只改变方向但不行进

常用RGB色彩

英文名称|RGB整数值|RGB小数值|中文名称
:---:|:---:|:---:|:---:|
white|255, 255, 255|1, 1, 1|白色
yellow|255, 255, 0|1, 1, 0|黄色
magenta|255, 0, 255|1, 0, 1|洋红
cyan|0, 255, 255|0, 1, 1|青色
blue|0, 0, 255|0, 0, 1|蓝色
black|0, 0, 0|0, 0, 0|黑色
seashell|255, 245, 238|1, 0.96, 0.93|海贝色
gold|255, 215, 0|1, 0.84, 0|金色
pink|255, 192, 203|1, 0.75, 0.80|粉红色
brown|165, 42, 42|0.65, 0.16, 0.16|棕色
purple|160, 32, 240|0.63, 0.13, 0.94|紫色
tomato|255, 99, 71|1, 0.39, 0.28|番茄色

turtle RGB色彩模式默认小数值，可切换 `turtle.colormode(mode)`

### import 用法

- import <库名>   使用 => <库名>.<函数吗>(<函数参数>)
- from <库名> import <函数名>
- from <库名> import *
- import <库名> as <库别名>     使用 => <库别名>.<函数名>(<函数参数>)

### 数值运算函数

函数及使用|描述
:---:|:---
abs()|绝对值
divmod(x,y)|返回商余(X//Y,X%Y)
pow(x,y[, z])|幂余(x**y)%z，[...]参数z可省
round(x[,d])|四舍五入，d为保留小数位数
max(a,b,c,,,,n)|返回数组最大值
min(a,b,c,,,,n)|返回最小值
int(x)|将x变成整数，舍弃小数部分
float(x)|将x变成浮点数
complex(x)|将x变成复数，增加虚数部分：complex(4) => 4 + 0j

### 字符串处理函数

函数及使用|描述
---|---
len(x)|获取字符串长度
str(x)|将任意类型x转换为字符串形式
hex(X) 或 oct(x)|整数x的十六进制或八进制小写形式字符串
chr(u)|x为Unicode编码，返回其对应的字符
ord(x)|返回字符x的Unicode编码

### 字符串处理方法

> "方法"在编程中是一个专有名词

- "方法"特指 <a>.<b>() 风格中的函数 <b>()
- 方法本身也是函数，但与<a>有关，
- 字符串及变量也是<a>，存在一些方法，

*In Python， 一切皆对象*

方法及使用|描述
---|---
str.lower() 或 str.upper()|返回字符串副本，且全部为小写/大写
str.split(sep=None)|返回以sep分割的str的列表
str.count(sub)|返回字符sub出现的次数
str.replace(old,new)|返回字符串副本，且所有old的字符换为new字符
str.center(width[,fillchar])|字符串str根据宽度width居中，fillchar可选<br> `"python".center(20,"=")`<br>结果为`=======python=======`
str.strip(chars)|返回没有chars的字符串
str.join(iter)|在iter变量除最后一个元素外，每个元素后加入一个str(可结合split用，)


### 字符串类型的格式化

<模版字符串 { <参数序号> : <格式控制标记>} >.format(<逗号分隔的参数>)

# 1.01^365 = 37.78  
# 1.019^365 = 962.89

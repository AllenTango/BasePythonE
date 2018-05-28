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

- "方法"特指 <a对象>.<b方法>() 风格中的函数 <b方法>()
- 方法本身也是函数，但与<a对象>有关，
- 字符串及变量也是<a对象>，存在一些方法，

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

## time 库

- 时间获取：time(), ctime(), gmtime()
- 时间格式：strftime(), strptime()
- 程序时间：sleep(), perf_counter()

### 格式化控制符

格式化字符串|日期/时间说明|值范围和实例
---|---|---
%Y|年份|0000～9999，例如：1900
%m|月份|01～12，例如：10
%B|月份名称|January～December，例如：April
%b|月份名称缩写|Jan～Dec，例如：Apr
%d|日期|01～31，例如：25
%A|星期|Monday～Sunday，例如：Wednesday
%a|星期缩写|Mon～Sun，例如：Wed
%H|小时(24制)|00～23，例如：12
%h|小时(12制)|01～12，例如：7
%p|上/下午|AM，PM，例如：PM
%M|分钟|00～59，例如：26
%S|秒|00～59，例如：26

## 程序的分支结构

- 顺序结构
- 分支结构
    - 单分支结构
    - 二分支结构
    - 多分支结构
    - 条件判断及组合
    - 程序的异常处理
- 循环结构

### 单分支结构

```python
if <条件>：
    <语句块>
```

```python
guess = eval(input())
# if True:
if guess == 99:
    print("猜对了")
```

### 二分支结构

```python
if <条件>:
    <语句块1>
else:
    <语句块2>
```

```python
guess = eval(input())
if guess == 99:
    print("猜对了")
else:
    print("猜错了")
```

二分支结构紧凑型：适用于简单表达式的二分支结构

`<表达式1> if <条件> else <表达式2>`

```python
guess = eval(input())
print("猜{}了".format("对" if guess == 99 else "错"))
```

### 多分支结构

需要注意多条件之间的包含关系
```python
if <条件1>:
    <语句块1>
elif <条件2>:
    <语句块2>
...
    ...
else:
    <语句块N>
```
需要注意变量去值范围的覆盖

### 条件组合：and、or、not

### 程序的异常处理

```python
try:
    <语句块1>
except:
    <语句块2>
```
```python
try:
    <语句块1>
except <异常类型>:
    <语句块2>
```
```python
try:
    <语句块1>
except:
    <语句块2>
else:
    <语句块3>
finally:
    <语句块4>    # 语句块4 一定会执行
```

```python
try:
    num = eval(input("请输入一个整数: "))
    print(num**2)
except NameError:
    print("输入不是整数")
    # 标注异常类型后，仅响应该异常
    # 异常类型名字等同于变量
```

### 程序的循环结构

- 遍历循环
    - 计数循环(N次)
    - 计数循环(特定次[M:N:K])
    - 字符串遍历循环
    - 列表遍历循环
    - 文件遍历循环
    - ......
        - 由保留字for和in组成，完整遍历遍历结构所有元素后结束
        - 每次循环，所获的元素放入循环变量，并执行一次语句块
- 无限循环
- 循环控制保留字
    - break 跳出并结束当前循环(break所在的循环)，执行循环后的语句
    - continue 结束当次循环，继续执行后续次数循环
- 循环高级用法(循环与else)
    - 当循环没有被break语句退出时，执行else语句块
    - else语句块作为"正常"完成循环的奖励
    - 这里else的用法与异常处理中else用法相似

遍历循环
```python
for <循环变量> in <遍历结构>:
    <语句块>
```

无限循环
```python
# 反复执行语句块，直到条件不满足
while <条件>:
    <语句块>
```

循环高级用法
```python
for c in "PYTHON":
    if c == "T":
        continue
    print(c, end="")
else:
    print("正常退出")

# >>> PYHON正常退出
```
```python
for c in "PYTHON":
    if c == "T":
        break
    print(c, end="")
else:
    print("正常退出")

# >>> PY
```

## random 库

### 基本随机数函数

函数|描述
:---:|:---
seed(a=None)|初始化给定的随机数种子，默认为当前系统时间 <br> 给定相同的随机种子，生成的随机数一定
random()|生成一个[0.0,1.0)之间的随机小数


### 扩展随机数函数

函数|描述
:---:|:---
randint(a,b)|生成一个[a,b]之间的整数
randrange(m,n[,k])|生成一个[m,n)之间以k为步长的随机整数
getrandbits(k)|生成一个k比特长的随机整数
uniform(a,b)|生成一个[a,b]之间的随机小数
choice(seq)|从序列seq中随机选择一个元素
shuffle(seq)|将序列seq中元素随机排列，返回打乱后的序列

# 函数——降低编程难度 & 代码复用

```python
# 一般函数定义
def <函数名>(<参数(0个或多个),(可变参数*b)>):
    <函数体>
    return <返回值>
```
- 所指定的参数为**占位符**
- 函数需 调用 方可执行
- 函数(IPO)：参数是输入、函数体是处理、结果是输出

```python
# 计算n！
def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
```

保留字 global 声明使用全局变量

## lambda 定义匿名函数

`<函数名> = lambda <参数>: <表达式>`   等价于
```python
def <函数名>(<参数>):
    <函数体>
    return <返回值>
```
lambda 函数如👉 `f = lambda x, y: x + y`
`f(10,15)   => 25`
*慎用lambda函数*，一般使用 def 定义普通函数


# 理解方法思维

- 模块化思维：确定模块接口，封装功能
- 规则化思维：抽象过程为规则，计算机自动执行
- 化繁为简：将打工能变为小功能组合，分而治之

## 代码复用与模块化设计

### 代码复用(把代码抽象成资源进行抽象)

函数和对象是代码复用的两种主要形式：
- 函数：将代码命名，在代码层面建立初步抽象
- 对象：属性和方法，`<a>.<b> 和 <a>.<b>()` <br>
在函数之上再次组织进行抽象

### 模块设计

- 分而治之
    - 通过函数或对象封装将程序划分为模块及模块间的表达
    - 具体包括：主程序、子程序和子程序间关系
    - 分而治之：一种分而治之、分层抽象、体系化的设计思想
- 紧耦合  松耦合
    - 紧耦合：两部分之间交流很多，无法独立存在
    - 松耦合：两个部分之间交流较少，可以独立存在
    - 模块内部紧耦合、模块之间松耦合
    
### 递归

- 链条：计算过程存在递归链条
- 基例：存在一个或多个不需要再次递归的基例

```python
# n! 阶乘
def fact(n):
    if n == 0:
        return 1
    else:
    return n*fact(n-1)
```

```python
# 将字符串s反转后输出
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]
```

```python
# 斐波那契数列
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
```
```python
# 汉诺塔
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
```
使用 pyinstaller 转为 可执行文件 `pyinstaller -i Turtle.ico -F pyIn.py`

## 集合
- 集合，无序，唯一，不可更改
- 集合用打括号 `{}` 表示，元素间用逗号分隔
- 建立集合类型用 `{}` 或 `set()`
- 建立空集合类型，必须使用set()

集合操作符

操作符及应用|描述
---|---
`S🌲T`|并，返回S、T的并集合为新集合
`S-T`|差，返回在S但不在T中的新集合
`S&T`|交，返回S和T的交集为新集合
`S^T`|补，返回S和T的非相同元素的新集合
`S<=T` 或 `S<T`|返回True/False，判断S和T的子集关系
`S>=T` 或 `S>T`|返回True/False，判断S和T的包含关系
`S🌲=T`|更新集合S=S🌲T
`S-=T`|更新集合S=S-T
`S&=T`|更新集合S=S&T
`S^=T`|更新集合S=S^T

集合处理方法
操作函数或方法|描述
---|---
S.add(x)|新增元素x
S.discard(x)|移除元素x
S.remove(x)|移除元素x，会包KeyError异常
S.clear()|移除S中所有元素
S.pop()|随机返回S中的一个元素，更新S，若S为空产生KeyError异常
S.copy()|返回集合S的一个副本
len(S)|返回集合S的元素个数
x in S|判断元素x是否在集合S中
x not in S|判断元素x是否不在集合S中
set(x)|将其他类型变量x转变为集合类型

## 序列类型

- 字符串类型
- 元组类型
- 列表类型



# 1.01^365 = 37.78  
# 1.019^365 = 962.89

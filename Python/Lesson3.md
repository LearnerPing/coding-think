# 随机数和变量、循环进阶
## 随机数模块
python还提供了很多模块，用来实现各种常见的功能，比如时间处理、科学计算、网络请求、随机数等等等等。这个时候我们不需要自己再去写这些模块，只需要引用使用就行了

引入模块的方法：
~~~
from 模块名 import 方法名
~~~
外部模块的引用现阶段不要求具体去理解，就现在知道我要使用随机数的话在代码最上面这么写就好了
~~~
from random import randint
~~~
下面这段代码会产生一个1~100 之间的随机数
~~~
num = randint(1, 100)
~~~
针对随机数，我们写一个猜数字的小游戏
~~~
from random import randint, random

randomNum = randint(1,100)
print("输入一个数字，猜对不对")
num = int(input())

while num != randomNum :
    if(num > randomNum) :
        print("数字大了，请再次输入")
    else :
        print("数字小了，请再次输入")
    num = int(input())
print("Bingo! 猜对了，数字是%s" %randomNum)
~~~

## 变量进阶
变量名不是你想起就能起的：

* 第一个字符必须是字母或者下划线_
剩下的部分可以是字母、下划线_或数字0~9
* 变量名称是对大小写敏感的，myname 和 myName 不是同一个变量。

几个有效的栗子
~~~
i
__my_name
name_23
a1b2_c3
~~~
几个会报错的栗子（记得对照上面的规则想下为啥不对）
~~~
2things
this is spaced out
my-name
~~~

前面知道了变量可以赋值也可以传递表达式的结果，然后关于运算有一些简单的缩写
~~~
a += 3
~~~
他的含义等价于 a = a + 3

在我们前面的猜数字游戏上拓展一下，输出一下猜了多少次
~~~
from random import randint, random
randomNum = randint(1,100)
print("输入一个数字，猜对不对")
num = int(input())
count = 1
while num != randomNum :
    if(num > randomNum) :
        print("数字大了，请再次输入")
    else :
        print("数字小了，请再次输入")
    num = int(input())
    count += 1
print("Bingo! 猜对了，数字是%s" %randomNum)
print("一共猜了%s次" %count)
~~~

## 逻辑判断进阶
首先，要理解，一个逻辑表达式，其实最终是代表了一个bool类型的结果，比如：  1 < 3 这就相当于是一个 True 值，2 == 3 就相当于是一个 False 值

同样，举个栗子：
~~~
a = 1
print(a>3)  #False
print(a==2-1)  #True
b = 3
print(a+b==2+2)  #True
~~~
比较容易搞混的，是bool变量的值和一个逻辑表达式的值，比如：
~~~
a = False
print(a)  #False
print(a==False)  #True
~~~
虽然 a 本身的值是 False，但是 a==False 这个表达式的值是True

一个小测试，顺便理解下与或非 下面这些表达式，输出的结果是什么呢？
（可以自己写代码 print一下）
~~~
b
not b
a == b
a != b
a and b
a or b
1<2 and b==True
~~~

## 循环进阶 For
同 while 一样，for 循环可以用来重复做一件事情。在某些场景下，它比 while 更好用。
类比我们前面写的那个累加
如果用for循环，则可以这么写：
~~~
sum = 0 
for i in range(1, 101):
    sum += i 
print(sum)
~~~
解释一下，range(1, 101) 表示从1开始，到101为止（不包括101，注意这里和 randint 不一样），取其中所有的整数。

for i in range(1, 101) 就是说，把这些数，依次赋值给变量i。

***作业***：
 * （简单版）输入一个值，输出以这个值为公比，1为首项的等比数列前10项.例：

输入

2


输出

1

2

4

8

16

32

64

128

256

512

 * （地狱难度版）输入一个大于等于3的值n，输出斐波纳契数列的前n项。注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和用 for 循环实现(比较难，可以先不做等讲解)
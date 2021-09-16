# Lesson 2:基础知识补充和基本逻辑判断介绍
## IDE介绍
 IDE，英文叫做 Integrated Development Environment，中文就是集成开发环境，简单来说，你要去写文章的话，用什么笔，用什么本子，这些文具一套合成在一起就叫IDE。 PS就是图片的IDE，Excel就是.xls文档的IDE
 关于python常见的IDE有 PyCharm 、VSCode，因为VSCode集成兼容了很多其他的内容，所以这里使用VSCode
## 输入输出
程序和用户之间的交互通过输入输出来实现
python有一个接收命令行下输入的方法：
~~~
input()
~~~
一个简单的例子
~~~
print("Who do you think I am?")
input()
print("Oh, yes!")
~~~
代码会在运行到 input的时候停下来，等待用户的输入，输入后才会进行下一步
* 注意：py3里的input()得到的都是字符串。输入数字也会被认为是字符串
## 变量
变量，望文生义，就是可变化的量，我们在代码里面通过创建变量存储各种不同的值
举个栗子
~~~
name = 'Ping'
myVar = 123
price = 5.99
visible = True
~~~
通过等号将右边的值赋予左边的变量

这里说一下另外一个概念，叫做“数据类型”，上面4颗栗子分别代表了python中较常见的四种基本类型：

* 字符串 ： 表示一串字符，需要用''单引号或""双引号包围起来
* 整数
* 浮点数 ： 就是小数
* bool（布尔）： 这个比较特殊，是用来表示逻辑上的“真”和“假”（或者说“是”和“非”）的一种类型，它只有两个值，True 和 False。（注意：这里没有引号，有了引号就变成字符串了）

“=”的右边还可以更复杂一点，比如是一个计算出的值:
~~~
value = 3 * 4
print(value)
value = 2 < 5
print(value)
~~~
* 对应值恒定不变的叫常量 数字、字母 都是常量，不可以被再次赋值

## 逻辑判断
逻辑判断对应的主要就是 bool 值，也就是 true/false 真和假，复杂的业务都是建立在这个基础上的，看下面的栗子
~~~
a = 1 < 3
print(a)
b = 1
c = 3
print(b > c)
~~~
通过用“>”“<”来比较两个数值，我们就得到了一个bool值。这个bool值的真假取决于比较的结果。

“>”“<”在编程语言中被称为比较运算符（或叫 关系运算符），常用的比较运算符包括：

* '>' 大于
* '<'	小于
* '>='	大于等于
* '<='	小于等于
* '=='	等于（比较两个值是否相等。之所以用两个等号，是为了和变量赋值区分开来）
* '!='	不等于

还有一种逻辑运算符：
* not  ;逻辑“非”	如果 x 为 True，则 not x 为 False
* and ;逻辑“与”	如果 x 为 True，且 y 为 True，则 x and y 为 True
* or  ;逻辑“或”	如果 x、y 中至少有一个为 True，则 x or y 为 True

把最开始的代码复杂化一下
~~~
num = 10
print('你想输入什么?')
answer = int(input())

result = answer<num
print('太小了?')
print(result)

result = answer>num
print('太大了?')
print(result)

result = answer==num
print('等于？')
print(result)
~~~

## 逻辑判断
下面展示的是基本的IF判断逻辑
* ![avatar](https://cdn.py2china.cn/wechat/pystart/7-0.png)

基本语法为：
~~~
if 条件:
    选择执行的语句
~~~

* 注意：条件后面的冒号不能少，同样必须是英文标点。
* 加强注意：if 内部的语句需要有一个统一的缩进（就是指每一行开头的空格），一般用4个空格（可以按 Tab 键添加）。缩进表示这些代码属于这个 if 条件内部，是一个“代码块”。python用这种方法替代了其他很多编程语言中的大括号{}。

举个栗子
~~~
age = int(input())
if age >= 18:
    print("你是个成年人了！")
~~~



**作业** ：结合if 实现 输入一个数字，让代码判断是大于10 还是小于10 还是等于 10，并输出结果


## While判断
先添加一个小知识：python里，以“#”开头的文字会被忽略，不会被认为是可执行的代码。在VScode 里面可以选中代码段 按 Ctrl + k + c 整段注释

下面介绍的是循环

* ![avatar](https://cdn.py2china.cn/wechat/pystart/8-0.png)

程序执行到 while 处，“当”条件为 True 时，就去执行 while 内部的代码；“当”条件为 False 时，就跳过。

语法为：
~~~
while 条件:
    循环执行的语句
~~~

新的栗子:
~~~
a = 1             # 为了后面的条件能满足，先把a设为1
while a != 0:     # 如果a不等于0就循环（1不等于0）
    print("please input")
    a = int(input())     # 在循环内部获取输入，改变a的值
print("over")
~~~
程序执行后，会不断向你询问输入，直到你输入0，条件 a!=0 不满足，循环结束。

**作业**：循环输出1~100的和
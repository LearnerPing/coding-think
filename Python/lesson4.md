# 字符串
## 字符串初步讲解
字符串就是一组字符的序列。python中最常用的字符串表示方式是单引号（''）和双引号（""），但是两者的含义是一样的，比如，'string' 和 "string" 对于 Python 来说效果是一样的。
如果你想表示一段带有英文单引号或者双引号的文字，那么表示这个字符串的引号就要与内容区别开。
内容带有单引号，就用双引号表示,三个引号（'''）或者（"""）于此类似
~~~
"It's good"
'You are a "BAD" man'
'''
"What's your name?" I asked.
"I'm Han Meimei."
'''
~~~
另外还有一种方法，就是使用转义符\
~~~
'I\'m a \"good\" teacher'
~~~

\ 被称作转义字符，除了用来表示引号，还有比如用
* \n 表示字符串中的换行（相当于按一下回车键的效果）
* \t 表示字符串中的制表符（相当于按一下tab键的效果）
* \\ 表示字符串中的 \ （因为单个斜杠被用来做转义了，所以真的要表示 \ 字符，就要两个斜杠）
* 用来在代码中换行，而不影响输出的结果
~~~
"this is the \
same line"
~~~
## 字符串格式转换
### 拼接字符串
如果你想把两段字符连起来输出，你可以有下面几种方式加起来
~~~
str1 = 'good'
str2 = 'bye'
print(str1 + str2)
print('very' + str1)
print(str1 + ' and ' + str2)
~~~
不过数字是不能直接和字符串相加，可以通过转换数据格式实现拼接
~~~
num = 18
print('My age is' + num)#报错
print('My age is' + str(18))
print('My age is' + str(num))
~~~
还有一种方法，就是用 % 对字符串进行格式化
~~~
num = 18
print('My age is %d' % num)
print('Price is %.2f' % 4.99)
name = 'Ping'
print('%s is a good Player.' % name)
print('Today is %s.' % 'Holiday' )
~~~
这里，%d 只能用来替换整数。如果你想格式化的数值是小数，要用 %f，%s是字符串，另一个%后面就是你要格式化的值

## 循环嵌套
既然提到了字符串，就顺便讲下输出
结合之前的学习，如果我们要输出5个 *，用 for 循环可以这么写：
~~~
for i in range(0, 5):
    print('*')
~~~
如果想让这5个*在同一行，需要加上 end 参数，使得 print 之后不换行：
~~~
for i in range(0, 5):
    print('*', end=' ')
~~~
如果要输出特殊格式比如这样的怎么办：
~~~
*
**
***
****
*****
~~~
自己动手打好一个多行字符串明显是很愚蠢的方式，我们需要的是一个两个嵌套在一起的循环：
~~~
for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end=' ')
    print()
~~~
可以观察下下面这段代码的输出，看看是如何变化的
~~~
for i in range(0, 3):
    for j in range(0, 3):
        print(i, j)
~~~
第二个 for 循环在第一个 for 循环的内部，表示每一次外层的循环中，都要进行一整遍内层的循环。

***作业:*** :输出乘法表
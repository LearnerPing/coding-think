# 类型转换
## 字符串格式化 补充
之前我们说到，可以用%来构造一个字符串，比如
~~~
print ('%s is easy to learn' % 'Python')
~~~
但是当你需要一个同事匹配多个字段内容的时候可以使用：
~~~
print("%s's score is %d" % ('Mike', 87))
~~~
括号内的内容称为元组，属于一种数据结构，无论你有多少个值需要代入字符串中进行格式化，只需要在字符串中的合适位置用对应格式的%表示，然后在后面的括号中按顺序提供代入的值就可以了。占位的%和括号中的值在数量上必须相等，类型也要匹配。

## 类型转换
之前有提到多个基本数据类型
- 字符串
- 整数
- 小数 （浮点数）
- bool类型
Python是弱语言类型代码，定义一个变量时不需要给它限定类型。变量会根据赋给它的值，自动决定它的类型。你也可以在程序中，改变它的值，于是也就改变了它的类型。
~~~
a = 1
print(a, type(a))
a = 'hello'
print(a, type(a))
a = True
print(a, type(a))
~~~
变量 a 先后成为了整数int、字符串str、bool类型。
不同类型的数据之间直接运算会出现错误，为了应对
这种情况下，python提供了一些方法对数值进行类型转换：

- int(x)     #把x转换成整数
- float(x)  #把x转换成浮点数
- str(x)     #把x转换成字符串
- bool(x)   #把x转换成bool值
~~~
print ('Hello'+str(1))
print ('hello%d' % int('123'))
~~~
当然，并不是所有的值都能做类型转换，比如 int('abc') 同样会报错，因为 python 没办法把它转成一个整数。
## bool 的类型转换
在python中，其他类型转成 bool 类型时，以下数值会被认为是False：
- 为0的数字，包括0，0.0
- 空字符串，包括''，""
- 表示空值的 None
- 空集合，包括()，[]，{}

其他的值都认为是True。

None 是 python 中的一个特殊值，表示什么都没有，它和 0、空字符、False、空集合 都不一样

*** 作业 ***：

1.输出最大值，让用户输入三个数值，然后输出其中的最大值

2.输出从1000以内，用3、5、7去除，余数均为2的正整数。
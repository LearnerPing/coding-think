print("输入第一个数")
a = int(input())
print("输入第二个数")
b = int(input())
#开始循环取余数,因为这里循环次数是未知的，所以我们使用while
while a%b!=0:
    num = a%b #交叉赋值
    a = b
    b = num #这段可以简写为 a,b=b,(a%b)
print("最大公约数为%d" % b)
#第二章编程题

#1 获得用户输入的一个整数N，计算并输出N的32次方
N=eval(input("输入一个数字："))
i=1
n=N
while i<32:
	x=N+N
	N=x
	print("第{}次b的值是：{}".format(i,N))
	i=i+1
print("N的32次")

print(n**32)

'''
#2 获得用户输入的一段文字，将这段文字进行垂直输出。
str=input("输入一段文字：")
i=len(str)

#方法1
i=-(i+1)
i=i+1
while i<0:
	print(str[i])
	i=i+1

#方法2
x=0
while x<i:
	print(str[x])
	x=x+1
'''

'''
#3 获得用户输入的一个合法算式，列如：1.2+3.4，输出运算结果
str=input("输入一个算式")
print (str.split('+',2))

s=eval(str)
print("{}+{}={}".format(str[1],str[2],s))
'''

'''
#4获得用户输入的一个小数，提取并输出其整数部分
str=input("输入一个小数")
s=int(eval(str))
print(s)
'''
'''
#改错题
#n=input("请输入整数N:");
#sum=0
#for i in range(n)
#	sum + = i+1
#print("1到N求和结果："format(sum))

n=eval(input("请输入整数N:"));
sum=0
for i in range(n):
	#i= i+1
	#sum =sum+i
	sum + = i + 1
print("1到N求和结果：{}".format(sum));
'''

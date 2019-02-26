#1.实现isNum()函数，参数为一个字符串，如果这个字符串属于整数、浮点数或负数的表示，则返回True，否则返回False
'''
def isNum():

	try:
		a = eval(input())

		if type(a) == int or type(a) == float or type(a) == complex:
			print('True')
		else:
			print('False')

	except:
		print('False')

isNum() 
'''

'''
#2.实现isPrime()函数，参数为整数，要有异常处理。如果整数是质数，返回True，否则返回Fales（只能被1和本身除尽的数）
def isPrime():
	while True:
		count=0
		try:
			a=int(input("输入整数"))
		except:
			print("输入内容必须为整数")
			continue
		for i in range(1,a+1):
			#print("i的值是",i,"a的值是",a)
			if a%i==0:
				count+=1
		if count==2:
			print(a,"是质数")
		else:
			print(a,"不是质数")

isPrime()
'''
'''
#3.编写一个函数，统计不同字符个数。用户从键盘输入一行字符，统计并输出其中英文、数字、空格、其它字符的个数

def countstr():
	sz=zm=kg=qt=0
	strs=input("请输入字符串")
	for i in strs:
		if i>="0" and i<="9":
			sz+=1
		elif (i>="a" and i<="z") or (i>="A" and i<="Z"):
			zm+=1
		elif i==" ":
			kg+=1
		else:
			qt+=1
	print("数字有",sz,"个，字母有",zm,"个，空格有",kg,"个，其它有",qt,"个")

countstr()

'''
'''
#4.编写一个函数，打印200以内的所属素数，以空格分割。
def isPrime200():

	for n in range(1,201):
		#print("n:",n)
		count=0
		for i in range(1,n+1):
				#print("i的值是",i,"a的值是",a)
			if n%i==0:
				count+=1
		if count==2:
			print(n,end=' ')
		else:
			continue

isPrime200()
'''

#5.编写一个函数，参数为一个整数n，利用递归获取斐波拉契数列中的第n个数并返回

def Fibonacci():
	n=int(input("输入一个整数"))
	a,b=0,1
	for i in range(n):
		a,b=a+b,a
		#print(a,end=" ")
	return a,n
re=Fibonacci()
print(re[1],"返回数是：",re[0])
#print("返回数是：",Fibonacci())

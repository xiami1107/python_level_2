#第四章编程题

#1.输入年份，判断闰年
'''
while True:
	year=eval(input("请输入一个年份"))
	if year%4==0:
		if year%100!=0:
			print(year)
			print("是闰年\n") 
			continue
	if year%400==0:
		print(year)
		print("是闰年\n")
	else:
		print(year)
		print("不是闰年\n")
	if year==0:
		break
'''

#2.获得连个整数，就出这两个整数的最大公约数和最小公倍数
a=eval(input("请输入第一个数"))
b=eval(input("请输入第二个数"))


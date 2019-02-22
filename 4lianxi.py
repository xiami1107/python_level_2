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
'''求两个数的最大公约数时，先用较大数除以较小数，如果能整除，最大公约数就等于较小数；
否则用较小数除以第一步的余数，如果能整除，最大公约数就等于第一步的余数；
否则，用当前获得的余数除以上一步的余数，直到能整除为止。
此时作为除数的那个数就是最开始那两个数的最大公约数。'''
'''
#最大公约数

a=int(input("请输入第一个数"))
b=int(input("请输入第二个数"))
if a>b:
	smaller=b
else:
	smaller=a
for i in range(1,smaller+1):
	if ((a%i==0) and (b%i==0)):
		hcf=i
		print(i)
print(a,"和",b,"的最大公约数是",hcf)

#最小公倍数（两个数的和除以最大公约数）

i=a*b/hcf
print(a,"和",b,"的最小公倍数是",i)
'''

#3.统计不同字符个数。用户从键盘输入一行字符，统计并输出其中英文、数字、空格、其它字符的个数
sz=zm=kg=qt=0
for i in input("请输入字符串"):
	if i>="0" and i<="9":
		sz+=1
	elif (i>="a" and i<="z") or (i>="A" and i<="Z"):
		zm+=1
	elif i==" ":
		kg+=1
	else:
		qt+=1
print("数字有",sz,"个，字母有",zm,"个，空格有",kg,"个，其它有",qt,"个")


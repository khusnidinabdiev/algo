import math
a,b,c,d=map(int, input().split())
x=float(input())
try:
	f=(a*x*x+b*x+c)/(a*a*(x*a+1)+pow(a,b-c))
	k=math.cos(abs((a*x+b)/(x*c+d+pow(2,c))))
except Exception as e:
	f=0
	k=0
else:
	print(format(f+k, '.2f'))

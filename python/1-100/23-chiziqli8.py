import math
a,b,c,d,x=map(float, input().split())
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a==0 or x*a+1+pow(a,b-c-2)==0:
	if c*x+d+pow(2,c)==0:
		print(format(0, '.2f'))
	else:
		f=math.cos(abs((a*x+b)/(x*c+d+pow(2,c))))
		print(format(f, '.2f'))
elif c*x+d+pow(2,c)==0:
	f=(a*x*x+b*x+c)/(a*a*a*x+a*a+pow(a,b-c))
	print(format(f, '.2f'))
else:
	f=(a*x*x+b*x+c)/(a*a*a*x+a*a+pow(a,b-c))+math.cos(abs((a*x+b)/(x*c+d+pow(2,c))))
	print(format(f, '.2f'))    

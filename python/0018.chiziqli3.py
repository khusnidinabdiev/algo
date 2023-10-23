import math

x,y=map(float, input().split())
u=1/(x+2/(x*x)+3/(x**3))+math.exp(x*x+3*x)
p=math.atan(x+y)+math.pow(5+x,2)
o=pow(math.cos(y*y+x*x/2),2)
print(format(u/p-o,'.2f'))
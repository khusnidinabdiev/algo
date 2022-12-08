import math
x,y=map(float, input().split())
t=1/(x+2/(x*x)+3/(x*x*x))+math.exp(x*x+3*x)
p=math.atan(x+y)+pow(abs(5+x),2)
k=pow(math.cos(y*y+x*x/2), 2)
print(format(t/p-k, '.2f'))
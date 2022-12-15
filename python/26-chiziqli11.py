import math
a,x,y=map(float, input().split())
a=int(a)
s=math.sqrt(math.exp(x*y)-x*math.sin(a*x)-(x*x+2)/(abs(x)+5))+math.sqrt(math.log(x*x+2)+5)
print(format(s,'.2f')) 

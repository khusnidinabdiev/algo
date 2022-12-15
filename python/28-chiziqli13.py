import math
a,x=map(float, input().split())
a=int(a)
s=x*math.sin(x/2+x/3+x/4)+(math.log(x*x-2)/math.log(10)+pow(3,a))/(math.cos(x+3)*math.sin(x+3)+8)
print(format(s,'.2f'))    

import math
x,y=map(float, input().split())
f=(2*math.tan(x+math.pi/6))/(1/3+math.cos(y+x*x)*math.cos(y+x*x))+math.log(x*x+2)/math.log(2)
print(format(f, '.2f'))
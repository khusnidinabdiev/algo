import math
x,y=map(float, input().split())
a=2*math.sin(x+math.pi/6)/math.cos(x+math.pi/6)/(1/3+pow(math.cos(y+x*x), 2))+math.log(x*x+2)/math.log(2)
print(format(a, '.2f'))
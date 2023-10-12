import math
x,y=map(float, input().split())

c1 = (x+y)/(y*y+math.fabs((y*y+2)/(x+x**3/5)))+math.exp(y+2)
print(format(c1, '.2f'))
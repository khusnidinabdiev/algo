import math
x,y=map(float, input().split())
c=(x+y)/(y*y+abs((y*y+2)/(x+x*x*x/5)))+math.exp(y+2)
print(format(c, '.2f'))
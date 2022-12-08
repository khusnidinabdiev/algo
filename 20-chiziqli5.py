import math
x,y=map(float, input().split())
f=(x*x+1)/(x*x+(x*y+y*y)/(y*y+(y+x*y)/(abs(x*y)+5)))+1/(1+math.cos(x)+1/(math.sin(abs(x))))
print(format(f, '.2f'))
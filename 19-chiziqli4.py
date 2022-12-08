import math
x,y=map(float, input().split())
f=abs(math.log(pow(x+y,2)+math.sqrt(abs(y)+2)-x+(x*y)/(x*x/2-5)))+pow(math.cos(x+y),2)/(pow(x+y,1/3))
print(format(f, '.2f'))
import math
a,x,y=map(float, input().split())
a=int(a)
z=math.sqrt(y*y+math.exp(x)+math.sqrt(math.exp(x)+a/(x*x+2))+pow(math.cos(x),2)/math.sin(x*x))+pow(math.cos(x),3);
print(format(z,'.2f'))
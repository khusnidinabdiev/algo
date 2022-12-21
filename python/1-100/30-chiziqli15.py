import math
x,y,z=map(float, input().split())
f=pow(2,-int(x))*math.sqrt(int(x)+pow(abs(y)+2,1./4.))*pow(math.exp(int(x)-1)/math.sin(z+2)+2,1./3.)
print(format(f, '.2f')) 
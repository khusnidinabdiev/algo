import math

x1,x2,c,d=map(float, input().split())
f=math.fabs(pow(math.sin(c*x2*x2*x2+d*x1*x1*x1-c*d),2)/math.sqrt(c*x1*x1+d*x2*x2+7))+math.tan(x1*x2*x2+d*d*d)
print(format(f,'.2f'))
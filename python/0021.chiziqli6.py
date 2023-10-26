import math


a,b = map(float, input().split())
t=pow(a,1/5)+pow(b*(a+b)/(2*b+a*b),1/4)*(a*a+b*b+2)

print(format(t, '.2f'))
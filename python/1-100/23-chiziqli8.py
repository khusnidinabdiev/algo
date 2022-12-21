import math
a,b,c,d,x=map(float, input().split())
a=int(a)
b=int(b)
c=int(c)
d=int(d)
f=(a*x*x+b*x+c)/(a*a*(a*x+1)+a**(b-c))+math.cos(abs((a*x+b)/(x*c+d+2**c)))

print(format(f, '.2f'))    





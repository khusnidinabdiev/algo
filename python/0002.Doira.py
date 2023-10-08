import math
a,b,c = map(float, input().split())
a=a*a*math.pi
a=format(a,'.2f')
b=b*b*math.pi
b=format(b, '.2f')
c=c*c*math.pi
c=format(c, '.2f')
print(f"{a} {b} {c}")    
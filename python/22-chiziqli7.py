import math
a,b,c,d=map(float, input().split())
f=abs(pow(math.sin(abs(c*pow(b,3)+d*pow(a,3)-c*d)),2))/math.sqrt(c*a*a+d*b*b+7)+math.tan(a*b*b+d*d*d)
print(format(f, '.2f'))
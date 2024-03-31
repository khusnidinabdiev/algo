import math
a,x=map(float, input().split())
d=(math.sqrt(x-1)+math.sqrt(x+2)+math.log(math.sqrt(x*x*a)+2)/math.log(10))/(math.sqrt(math.sqrt(x+2)+math.sqrt(x+24)+x**5))
print(format(d,'.2f'))
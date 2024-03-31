import math
a,b,c,x=map(float, input().split())
w=3/4+(8.2*x*x+math.sqrt(math.fabs(x*x*x+3*x)+math.cos(x-2)))/(a/4+b/3+c/2+1)
print(format(w,'.2f'))
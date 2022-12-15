import math
a,b,c,x=map(float, input().split())
a=int(a)
b=int(b)
c=int(c)
w=0.75+(8.2*x*x+math.sqrt(abs(x*x*x+3*x)+math.cos(x-2)))/(a/4+b/3+c/2+1)
print(format(w, '.2f'))  
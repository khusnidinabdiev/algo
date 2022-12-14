import math
x=float(input())
x=math.sqrt((2*math.tan(x+2)-math.cos(x+pow(2,x)))/(1+pow(math.cos(x+2),2)))+math.sin(x*x)/(x*x+3)
print(format(x,'.2f'))
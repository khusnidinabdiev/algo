import math
a,x=map(float, input().split())
a=int(a)
t=(pow(x-1,1/2)+pow(x+2,1/2)+math.log(x*pow(a, 1/2)+2)/math.log(10))/pow(pow(x+2,1/2)+pow(x+24,1/2)+pow(x,5),1/2)
print(format(t, '.2f'))  
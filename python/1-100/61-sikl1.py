import math
n=int(input())
s=0
for i in range(1,n+1):
	s+=math.sin(i)/pow(2,i)

print(format(s, '.2f'))   
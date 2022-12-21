import math
n=int(input())
s=0
for i in range(n):
	s+=pow(-1,i)*math.sin(pow(i+1,i+1))/pow(2,i+1)

print(format(s, '.2f'))
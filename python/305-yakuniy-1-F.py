x,n=map(int, input().split())
s=0
for i in range(1,n+1):
	s+=pow(x+1,1/i)
print(format(s, '.2f'))
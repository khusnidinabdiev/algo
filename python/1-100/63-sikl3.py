n=int(input())

s=0
p=1
for i in range(1,n+1):
	for j in range(1,2*i):
		p*=j
	s+=pow(-1,i-1)/p
	p=1
print(format(s,'.4f'))


n,x=map(int,(input().split()))

s=0
for i in range(1,n+1):
	s+=pow(-1,i-1)*1/pow(x,i*2)
print(format(s,'.3f'))


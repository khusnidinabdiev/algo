a,b,c=map(float, input().split())
if a<1 and b<1 and c<1:
	if a>b and b>c:
		print(a,b,a/2+b/2)
	elif a>c and c>b:
		print(a,a/2+c/2,c)
	elif b>a and a>c:
		print(a,b,a/2+b/2)
	elif b>c and c>a:
		print(b/2+c/2,b,c)
	elif c>a and a>b:
		print(a,a/2+c/2,c)
	elif c>b and b>a:
		print(b/2+c/2,b,c)
else:
	print(a,b,c) 
a,b,c=map(int, input().split())
if a>=0 and b>=0 and c>=0:
	print(a*a, b*b, c*c)
elif a>=0 and b>=0 and c<0:
	print(a*a,b*b,c)
elif a>=0 and b<0 and c<0:
	print(a*a,b,c)
elif a<0 and b<0 and c<0:
	print(a,b,c)
elif a<0 and b<0 and c>=0:
	print(a,b,c*c)
elif a<0 and b>=0 and c>=0:
	print(a,b*b,c*c)
elif a<0 and b>=0 and c<0:
	print(a,b*b,c)    
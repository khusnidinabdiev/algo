a,b,c=map(float, input().split())
if a<=3 and a>=1:
	if b<=3 and b>=1:
		if c<=3 and c>=1:
			print(a,b,c)
		else:
			print(a,b)
	elif c<=3 and c>=1:
		print(a,c)
	else:
		print(a)
elif b<=3 and b>=1:
	if c<=3 and c>=1:
		print(b,c)
	else:
		print(b)
else:
	print(c)
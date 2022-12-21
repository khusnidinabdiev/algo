x,y=map(int, input().split())
if x<y:
	print(format((x+y)/2,'.1f'),end=' ')
	print(format(4*x*y,'.1f'))
else:
	print(format(4*x*y,'.1f'),end=' ')	
	print(format((x+y)/2,'.1f'))
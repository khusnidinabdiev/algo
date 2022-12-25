x,y=map(float, input().split())
if x*x+y*y<=1 and x*x+y*y>=0.25:
	print('yes')
else:
	print('no')
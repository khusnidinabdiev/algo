x,y=map(float, input().split())
if x*x+y*y<=4 and x*x+y*y>=1 and y>=0:
	print('yes')
else:
	print('no')
x,y=map(float, input().split())
if x>=-1 and x<=1 and y>=-2 and y<=1:
	if y<=abs(x):
		print('yes')
	else:
		print('no')
else:
	print('no') 
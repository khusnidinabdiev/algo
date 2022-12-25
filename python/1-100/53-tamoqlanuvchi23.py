x,y=map(float, input().split())
if y>=0 and y<=1.5:
	if x>=-2 and x<=-1 and y>=1:
		print('yes')
	elif x>-1 and x<=0 and -x<=y:
		print('yes')
	elif x>0 and x<=1 and x<=y:
		print('yes')
	elif x>1 and x<=2 and y>=1:
		print('yes')
	else:
		print('no')
else:
	print('no')
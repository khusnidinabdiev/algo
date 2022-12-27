x,y=map(float, input().split())
if y<=1 and y>=-1:
	if x>=0 and x<=1:
		if 1.00/3.00*x-1.00/3.00>=y or y<=0:
			print('yes')
		else:
			print('no')
	elif x>=-1 and x<0:
		if 2*x+3<=y or -x>=y:
			print('yes')
		else:
			print('no')
	elif x>=-2 and x<-1:
		if 2*x+3<=y or 1.00/3.00*x-1.00/3.00>=y:
			print('yes')
		else:
			print('no')
	else:
		print('no')
else:
	print('no')


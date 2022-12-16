a,b,c=map(int, input().split())
if c<=b and b<=a:
	print(a*2,b*2,c*2)
else:
	print(abs(a),abs(b),abs(c))
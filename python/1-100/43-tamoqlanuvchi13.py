a,b=map(float, input().split())
if a<0 or b<0:
    if a<0 and b<0:
        print(abs(a),abs(b)) 
    else:
        print(a+0.5,b+0.5)
else:
    print(a,b)
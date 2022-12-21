x,y=map(float, input().split())
if y<=abs(1) and x>=-2 and x<=1:
    if x*x+y*y<=1 and abs(1/2*x+1)>=y:
        print("yes")
    else:
        print("no")
else:
    print("no")   
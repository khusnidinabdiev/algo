x,y=map(float, input().split())
if x>=-1 and x<=1 and y>=-1 and y<=2:
    if 3*x+2>=y and -3*x+2>=y:
        print('yes')
    else:
        print('no')
else:
    print('no')    

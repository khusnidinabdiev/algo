a,b,c,d=map(float, input().split())
if a<=b and b<=c and c<=d:
    print(d,d,d,d)
else:
    a=min(a,b,c,d)
    print(a,a,a,a)    
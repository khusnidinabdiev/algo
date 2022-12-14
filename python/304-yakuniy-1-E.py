a,b,c=map(float, input().split())
s=a+b+c
d=a*b*c
print(format(s/3*pow(a*b*c, 1/3), '.1f'))
a=float(input())
if a<-1:
    print(format(-a-1,'.2f'))
elif a>1:
    print(format(a-1,'.2f'))
elif a>-1 and a<=0:
    print(format(1+a,'.2f'))
else:
    print(format(1-a,'.2f'))    

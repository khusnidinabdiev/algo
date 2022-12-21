n=int(input())
inp=input()
s=map(int,inp.split())
su=sum(list(s))
orta=su/n
y=0
m=0
for i in map(int,inp.split()):
    if i<orta:
        y+=i 
        m+=1 
print(format(y/m,'.2f'))



#1
# l=[] 
# s=0
# n=int(input())
# for i in range(0,n):
#     e=int(input())
#     s+=e
#     l.append(e)
# s=s/n
# k=0
# a=0
# for i in range(0,n):
# 	if s>i:
# 		k+=i  
# 		a+=1
# print(k/a)  



#2
# n=int(input())
# l=list(map(int,input().split()))[:n] /////without [:n] is woking
# s=sum(l)
# av=s/n
# s=0
# k=0
# for i in l:
#     if i<av:
#         s+=i 
#         k+=1 
# print(format(s/k,'.2f'))



#3
# n = int(input())
# arr = input()
# l = list(map(int,arr.split()))
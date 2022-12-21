a=[]
n=int(input())
s=0
k=0
j=0
for i in range(0,n):
	ele = float(input())
	s+=ele
	a.append(ele)
s=s/n
for i in range(0,n):
	if s<a[i]:
		k+=a[i]
		j=j+1
print(format(k/j, '.2f'))



# n=int(input())
# a=list(map(int, input().strip().split()))[:n]
# print(a)




# lst = [ ]
# n = int(input("Enter number of elements : "))
  
# for i in range(0, n):
#     ele = [input(), int(input())]
#     lst.append(ele)
      
# print(lst)
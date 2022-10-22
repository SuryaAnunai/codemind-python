n=int(input())
l=[int(x) for x in input().split()]
even=0
for i in range(0,len(l),2):
    even+=l[i]
print(even)
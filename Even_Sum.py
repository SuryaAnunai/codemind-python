n=int(input())
l=[int(x) for x in input().split()]
even=0
for i in l:
    if i%2==0:
        even+=i
print(even)

n=int(input())
l=[int(x) for x in input().split()]
odd=0
for i in range(1,len(l),2):
    odd+=l[i]
print(odd)
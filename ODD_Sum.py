n=int(input())
l=[int(x) for x in input().split()]
odd=0
for i in l:
    if i%2!=0:
        odd+=i
print(odd)
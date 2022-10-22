n=int(input())
l=[int(x) for x in input().split()]
even=odd=0
for i in l:
    if i%2==0:
        even+=i
for i in l:
    if i%2!=0:
        odd+=i
print(abs(even-odd))
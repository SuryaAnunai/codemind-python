n=int(input())
max=0
while n>0:
    s=n%10
    if max<s:
        max=s
    n=n//10
print(max)
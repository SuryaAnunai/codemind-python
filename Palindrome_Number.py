t=int(input())
for i in range(t):
    num=int(input())
    temp=num
    rev=0
    while(num>0):
        d=num%10
        rev=rev*10+d
        num=num//10
    if(temp==rev):
        print("True")
    else:
        print("False")
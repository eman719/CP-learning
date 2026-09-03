t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    b=0
    cnt=0
    for i in range(n):
        if s[i]=="(":
            b+=1
        else:
            b-=1
        if b<0:
            cnt+=1
            b=0
    print(cnt)
            

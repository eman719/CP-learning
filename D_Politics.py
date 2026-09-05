t = int(input())
for _ in range (t):
    n,m= map(int,input().split())
    
    op= [input().strip() for b in range(n)]
    ans=0
    for a in op:
        if a==op[0]:
            ans +=1
    print(ans)
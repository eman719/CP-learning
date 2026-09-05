n,m=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
ans=0
for i in range(m):
    if p[i]<0:
        ans+=p[i]
    else:
        break
print(ans*-1)
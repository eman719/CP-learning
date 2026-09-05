n,d=map(int, input().split())
t=list(map(int, input().split()))
sing=sum(t)
rest=10*(n-1)
if d<sing+rest:
    print(-1)
else:#5+20
    jokes=((d-(sing+rest))//5)+(rest//5)
    print(jokes)

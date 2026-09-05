t = int(input())
for _ in range (t):
    l,r=map(int,input().split())
    a=r//2+1
    if a>=l:
        print(r%a)
    else:
        print(r%l)

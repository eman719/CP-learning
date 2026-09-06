num,t=map(int,input().split())
for i in range(t):
    if num%10==0:
        num//=10
    else:
        num-=1
print(num)
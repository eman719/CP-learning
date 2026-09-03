n= int(input())
k= int(input())
cnt=0
x=True
while k >n:
    if k%n!=0:
        x=False
        break
    else:
        x=True
        cnt+=1
    k=k/n
if x and k==n:
    print("YES")
    print(cnt)
else:
    print("NO")

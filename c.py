k,r=map(int,input().split())

for i in range (1,11):
    price=i*k
    if price%10==r or price%10==0:
        print(i)
        break
        
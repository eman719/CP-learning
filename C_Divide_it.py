t=int(input())
for _ in range (t):
    ans=0
    
    n=int(input())
    while n!=1:
      if n%2==0:
          n/=2
          ans+=1
      elif n%3==0:
         n=(n/3)*2
         ans+=1
      elif n%5==0:
         n=(n/5)*4
         ans+=1
      else:
         break
      
    if n!=1:
       print(-1)
    else:
       print(ans)
ta = "hello"
index = 0
s= input()
for i in range(len(s)):
    if ta[index]==s[i]:
        index+=1
    if index==5:
        break
if index==5:
    print("YES")  
else :
    print("NO")

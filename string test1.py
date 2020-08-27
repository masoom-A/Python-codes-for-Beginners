s=input()
n=int(input())
new_s=''
count=0
for i in range(0,n//len(s)):
    new_s+=s
new_s+=s[:n%len(s)]
for x in new_s:
    if x =='a':
        count+=1
print(count)
        

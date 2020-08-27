
def twoStrings(s1, s2):
    count=0
    for i in s1:
        for j in s2:
            if i==j:
                count+=1
    if count>0:
        return"Yes"
    else:
        return "No"

q = int(input())
for q_itr in range(q):
    s1=input().strip()
    s2=input().strip()
    print(twoStrings(s1, s2))

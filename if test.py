list1='12123124'
n=10
print((list1.count("1")*(n//len(list1))+(list1[:n%len(list1)]).count('1')))
#print((s.count('1')*(n//len(s))+(s[:n%len(s)]).count('a')))

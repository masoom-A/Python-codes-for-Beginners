def test(num):
    return((abs(1000-num)<=100) or(abs(2000-num)<=100))
i=int(input("enter the range"))
for x in range(0,i,1):
    num=int(input("enter a number"))
    print(test(num))

# contribution of each person
def food(f):
    tip=0.1*f
    f=f+tip
    eachperson=f/num
    return eachperson
def movie(m):
    mperson=m/num
    return mperson
num=int(input("enter the total person:"))
ftotal=int(input("enter toatal food cost:"))
mtotal=int(input("enter total amnt of tickets:"))
x=food(ftotal)
y=movie(mtotal)
print("totat contribution is:", x+y)

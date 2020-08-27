day=0
squats=0
total=0
print("enter the numbers of squats you did on each day for the last one week")
while day<=6:
    day=day+1
    squats=int(input("Total numbers of squats on day {}:".format(day)))
    total=total+squats
avg=total/day
print("the average squats you did in the last one week are {:.2f}:".format(avg))

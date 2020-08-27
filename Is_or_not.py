def string(str):
    if(len(str)>2 and str[:2]=="Is"):
        print("""string is start with "Is" """,str)
        return str
    else:
        print("Is"+str)
str=input("enter a string:")
string(str)

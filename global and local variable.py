age=7
def a():
    print("global variable 'age'",globals()['age'])
    globals()['age']=27
    print("modified global variable 'age'",globals()['age'])
    age=12
    print("local variable 'age'",age)
    return
a()
print("global variable is 'age' ",globals()['age'])

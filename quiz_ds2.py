x = [423,'b',37,'f']
u = x[1:]
print("u=",u)
y = u
w = x
u = u[0:]
u[1] = 53
x[2] = 47
print(x[2],y[1],w[2],u[1])

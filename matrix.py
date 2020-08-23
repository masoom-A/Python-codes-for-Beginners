def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]  
    list=[]
    for row in rez:
        list.append(row)
    return (list)
print(transpose([[1,2,3],[4,5,6]]))

def valley(list):
  if(len(list)==0):
    return(True)
  if(len(list)==1):
    return(False)
  if(list[0]<list[1]):
    return(False)
  for i in range(0,len(list)-1):
    if(list[i]<list[i+1]):
      pos=i
      break
    if(list[i]==list[i+1]):
      return(False) 
  else:
    return(False)
  for i in range(pos,len(list)-1):
    if(list[i]>=list[i+1]):
      return(False)
  return(True)
list=[]
for x in range (1,7):
    ele=input()
    list.append(ele)
    
print(valley(list))

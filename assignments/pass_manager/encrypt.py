p='ajay9991'

even= [p[i] for i in range(0,len(p),2)]
odd=  [p[i] for i in range(1,len(p),2)]
print(odd)
print(even)
ep=[]
for i in range(len(odd)):
    ep.append(odd[i])
    ep.append(even[i])
print(str(ep))
print(type(str(ep)))
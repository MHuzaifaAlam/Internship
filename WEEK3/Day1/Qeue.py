qeue=[]
qeue.append('A')
qeue.append('B')
qeue.append('C')
qeue.append('D')

print(qeue)

#peek Elemwnt
frontElement=qeue[0]
print(frontElement)

#deqeue
popedElement=qeue.pop(0)
print(popedElement)

print(qeue)

#Empty 
isempty=not bool(qeue)
print("The list is",isempty)

#length
isLength=len(qeue)
print("The qeue length is",isLength)


from collections import *
#Counter
print(Counter(['A','B','C','D']))
print(Counter({'A':3,'B':2,'C':3}))
print(Counter(a=3,b=5,c=8))

#namedtuple
person=namedtuple('Person',['name','age'])
s1=person('Jhon',30)
li=['Manjeet',19]
di = { 'name' : "Nikhil", 'age' : 19 }
print("The nametuple using iteratable  is : ")
print(person._make(li))
print ("The OrderedDict instance using namedtuple is  : ") 
print (s1._asdict()) 

#defaultdict
d=defaultdict(int)
L=[1,2,3,4,1,2,3,1,4,5,7,5]
for i in L:
    d[i]+=1

print(d)

d=defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary with Value List")
print(d)

#chain map
d1={'a':1,'b':2}
d2={'b':3,'c':2}
d3={'d':4,'e':5}
d4={'f':4,'g':5}

c=ChainMap(d1,d2,d3)
print(c)
print(c['a'])
print(c.values())
print(c.keys())
chain1=c.new_child(d4)
print("Displaying key map ")
print(chain1)

#deque
qeue=deque(['name','age','Dob'])
print(qeue)

de=deque([1,2,3,4])
de.append(5)
print("The deque after appending ")
print(de)
de.appendleft(6)
print("The deque after appending at the left is : ")
print(de)

#removing 
de=deque([6,1,2,3,4])
de.pop()
print("The Dequue after deleting from right is :")
print(de)

de.popleft()

print("The deque after deleting from left is : ")
print(de)




# Creating a dictionary where deletion is not allowed
class MyDict(UserDict): 
      
    # Prevents using 'del' on dictionary
    def __del__(self): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using pop() on dictionary
    def pop(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using popitem() on dictionary
    def popitem(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
      
# Create an instance of MyDict
d = MyDict({'a': 1, 'b': 2, 'c': 3})
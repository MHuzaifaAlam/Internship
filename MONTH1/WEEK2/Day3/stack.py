#basic stack with list 
st = []
st.append("a")
st.append("b")
st.append("c")

print(st)
print(st.pop())
print(st.pop())

# stack from deque
from collections import deque
st2=deque()
st2.append('a')
st2.append('b')
st2.append('c')
st2.append('d')

print(st2)
print(st2.pop())
print(st2.pop())
print(st2.pop())


print("From Lifo que")
# from lifoque
from queue import LifoQueue

st = LifoQueue()
st.put("a")
st.put("b")
st.put("c")

print(st.get())
print(st.get())
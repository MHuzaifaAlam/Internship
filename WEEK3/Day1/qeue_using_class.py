class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Qeue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.length = 0

    def enqeue(self, element):
        new_node = Node(element)
        if self.rare is None:
            self.front = self.rare = new_node
            self.length += 1
            return
        self.rare.next = new_node
        self.rare = new_node
        self.length += 1

    def deque(self):
        if self.isEmpty():
            return "Qeue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rare = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "the Qeue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQeue(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print()


myqeue = Qeue()
myqeue.enqeue('A')
myqeue.enqeue('B')
myqeue.enqeue('C')
myqeue.enqeue('D')
print("Qeue:", end="")
myqeue.printQeue()
print("Peek:",myqeue.peek())
print("Dequeue: ", myqeue.deque())
print("Queue after Dequeue: ", end="")
myqeue.printQeue()
print("isEmpty: ", myqeue.isEmpty())
print("Size: ", myqeue.size())

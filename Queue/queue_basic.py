
class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enque(self,value):
        "append"
        new_node = Node(value)
        temp=self.last

        if self.first is None or self.length == 0:
            self.first  , self.last = new_node, new_node
            
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
        return temp
    
    def dequeue(self):
        "pop first element"
        if self.first is None or self.length==0:
            return None
        if self.length == 1:
            self.first, self.last = None, None
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None

        self.length -=1
        return temp

            


my_queue = Queue(1)
my_queue.enque(2)
my_queue.dequeue()
my_queue.print_queue()  



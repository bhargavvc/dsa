

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None



class CircularSLL():
    def __init__(self): 
        self.head = None
        self.tail = None
  
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            if node.next == self.tail.next :
                break
            node = node.next    

    #creating First Node
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail   = node
        return 'CSLL has been created.'
    
    def insertCSLL(self,location,value):
        if self.head is None:
            return "Head is Empty."
        else:
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

            return "Node has been succefully inserted."
    

circularSingleLL = CircularSLL()
circularSingleLL.createCSLL(1)
circularSingleLL.insertCSLL(0,0)
circularSingleLL.insertCSLL(1,1)
circularSingleLL.insertCSLL(2,2)
circularSingleLL.insertCSLL(3,3)

print([node.value for node in circularSingleLL])


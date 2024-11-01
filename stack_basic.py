
class Node:
    def __init__(self,value):
        self.value =  value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node 
        # self.bottom = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self,value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
            
        else:
            new_node.next = self.top
            self.top = new_node

        self.height+=1
    
    def pop(self):

        if self.height == 0:
            return None
        else:
            if self.height == 1:
                self.top = None
            else:
                temp = self.top
                self.top = self.top.next
                temp.next = None
                self.height -= 1
        
            return temp.value  # Return the value of the popped node

    


# Example usage
my_stack = Stack(1)
print("Initial stack:")
my_stack.print_stack()  # Should print 1

my_stack.push(2)
my_stack.push(3)
print("\nStack after pushing 2 and 3:")
my_stack.print_stack()  # Should print 3, 2, 1

popped_value = my_stack.pop()
print(f"\nPopped value: {popped_value}")  # Should print 3
print("\nStack after popping:")
my_stack.print_stack()  # Should print 2, 1
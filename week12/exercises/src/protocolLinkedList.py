class Node:
     def __init__(self, data):
             self.data = data
             self.next = None

class LinkedList:
    def __init__(self):
            self.head = None

    def __len__(self):
        return len(self.head)

    def __add__(self, other):
        return self.head + other.head

def main():
    llist = LinkedList()
    llist.head = Node('Data of the first Node') 
    llist.head.next = Node('Data of second Node')

    
    print(llist)

main()



    
    
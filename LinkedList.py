class Node(object):
 
# Constructor 
 
    def __init__ (self, data, next = None):
        self.data = data
        self.next_node = next
 
# getters and setters
 
    def get_next (self):
        return self.next_node
 
    def set_next (self, next):
        self.next_node = next
 
    def get_data (self):
        return self.data
 
    def set_data (self, data):
        self.data = data
 
class LinkedList (object):
 
    def __init__(self, root = None):
        self.root = root
        self.size = 0
 
 
    def get_size (self):
        return self.size
 
    def add (self, data):
        new_node = Node (data, self.root)
        self.root = new_node
        self.size += 1
 
    def remove (self, data):
        this_node = self.root
        prev_node = None
 
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found
 
    def find (self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None
 
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))

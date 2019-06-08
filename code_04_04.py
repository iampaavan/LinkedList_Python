class SLLNode:
	
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def __repr__(self):
		return f"SLLNode Object: data={self.data}"
	
	def get_data(self):
		"""Return the self.data attribute."""
		return self.data
	
	def set_data(self, new_data):
		"""Replace the existing value of the self.data attribute with new_data parameter."""
		self.data = new_data
	
	def get_next(self):
		"""Return the self.next attribute"""
		return self.next
	
	def set_next(self, new_next):
		"""Replace the existing value of the self.next attribute with new_next parameter."""
		self.next = new_next


class SLL:
	
	def __init__(self):
		self.head = None
	
	def __repr__(self):
		return f"SLL Object: data = {self.head}"
	
	def is_empty(self):
		"""Returns True if the LinkedList is empty, otherwise returns False."""
		return self.head is None  # self.head == None
	
	def add_front(self, new_data):
		temp = SLLNode(new_data)
		temp.set_next(self.head)
		self.head = temp
	
	def size(self):
		"""Traverses the Linked List and returns an integer value representing the number of nodes
		in the Linked List."""
		
		"""The time complexity is O(n) because every Node in the Linked List must be visited in order
		to calculate size of the Linked List."""
		size = 0
		
		if self.head is None:
			return 0
		
		current = self.head
		while current is not None:
			size += 1
			current = current.get_next()
			
		return size
	
	def search(self, data):
		pass
	
	def remove(self, data):
		pass


sll = SLL()
print(sll.size())

sll.add_front(1)
sll.add_front(2)
sll.add_front(3)

print(sll.size())
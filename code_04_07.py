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
		"""Add a Node whose data is the new_data argument to the front of the Linked List."""
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
		"""Traverses the Linked List and returns True if the data searched for is present
		in one of the Nodes. Otherwise, it returns False."""
		"""Time Complexity is O(n) as we need to check every node in the Linked List to find the data."""
		if self.head is None:
			return f"Linked List is empty. No nodes to search."
		
		current = self.head
		while current is not None:
			# The Node's data matches what we're looking for
			if current.get_data() == data:
				return True
			# The Node's data doesn't match
			else:
				current = current.get_next()
		
		return False
	
	def remove(self, data):
		"""Removes the first occurrence of a Node that contains the data argument as its self.data variable.
		Returns nothing."""
		"""The time complexity is O(n) because in the worst case we have to visit every Node before we find the
		one we need to remove."""
		if self.head is None:
			return f"Linked List is empty. No Nodes to remove."
	
		current = self.head
		previous = None
		found = False
		
		while not found:
			
			if current.get_data() == data:
				found = True
		
			else:
				if current.get_next() == None:
					return f"A Node with that data value is not present."
				else:
					previous = current
					current = current.get_next()

		if previous is None:
			self.head = current.get_next()
			
		else:
			previous.set_next(current.get_next())
			
			
sll = SLL()
print(sll.remove(15))

sll.add_front(27)
print(sll.remove(15))

print(sll.head)
print(sll.remove(27))
print(sll.head)

sll.add_front('apple')
sll.add_front('berry')
sll.add_front('cherry')

print(sll.remove('berry'))
print(sll.head)
print(sll.head.next)

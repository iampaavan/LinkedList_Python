class DLLNode:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
	
	def __repr__(self):
		return f"DLL Object: data={self.data}"
	
	def get_data(self):
		"""Return the self.data attribute."""
		return self.data
	
	def set_data(self, new_data):
		"""Replace the existing value of self.data attribute with new_data parameter"""
		self.data = new_data
	
	def get_next(self):
		"""Return the self.next attribute"""
		return self.next
	
	def set_next(self, new_next):
		"""Replace the existing value of self.next with new_next parameter."""
		self.next = new_next
	
	def get_previous(self):
		"""Return the self.previous attribute"""
		return self.previous
	
	def set_previous(self, new_previous):
		"""Replace the existing value of self.previous with new_previous parameter."""
		self.previous = new_previous


class DLL:
	
	def __init__(self):
		self.head = None
	
	def __repr__(self):
		return f"DLL Object: head={self.head}"
	
	def is_empty(self):
		return self.head is None
	
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
	
	def add_front(self, new_data):
		"""Add a Node whose data is the new_data argument to the front of the Linked List."""
		temp = DLLNode(new_data)
		temp.set_next(self.head)
		
		if self.head is not None:
			self.head.set_previous(temp)
			
		self.head = temp
		
	def remove(self, data):
		pass

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
		pass
	
	def search(self, data):
		pass
	
	def add_front(self, new_data):
		pass
	
	def remove(self, data):
		pass

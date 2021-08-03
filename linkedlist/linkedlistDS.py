class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return f"Node({self.data}, {self.next})"
	__repr__ = __str__
	
class LinkedListds:
	def __init__(self, head=None):
		self.head = head

	def __len__(self):
		if self.head is None:
			return 0
		else:
			counter = 0
			t = self.head
			while t:
				counter += 1
				t = t.next
			return counter

	def getNode(self, data):
		if not self.head:
			return None
		t = self.head
		while t and t.data != data:
			t = t.next
		return t


	def isempty(self):
		return self.head is None

	def insert(self,data, pos=-1):
		n = Node(data)
		if pos > 0 and not self.head:
			raise Exception(f"cannot insert at {pos} on empty list")
		elif pos == -1 and not self.head:
			self.head = n
		elif pos == 0:			
			n.next = self.head
			self.head = n
		elif pos > -1 and self.head:
			counter = 0
			t = self.head
			while t != None and counter < pos:
				t = t.next
				counter += 1
			n.next, t.next = t.next, n
		else:
			t = self.head
			prev = None
			while t != None:
				prev = t
				t = t.next
			prev.next = n
	
	def traverse(self):
		t = self.head
		while t!= None:
			print(t.data, end=" ")
			t = t.next
	def remove(self, data):
		t = self.head
		prev = None
		if not t:
			return None
		if t.data == data:
			self.head = self.head.next
			m = t.data
			del t
			return m
		while t and t.data != data:
			prev = t
			t = t.next
		if t and prev:
			prev.next = t.next
			m = t.data
			del t
			return m
		else:
			raise Exception(f"{data} not found in list")
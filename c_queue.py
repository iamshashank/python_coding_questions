#list have pop(index) append(x)
class CQueue:
	def __init__(self,n):
		self.length = n
		self.count = 0
		self.front = 0
		self.rear = 0
		#self.queue = range(n)
		self.queue = []
		for i in range(0,5):
			self.queue.append(0)
	def enqueue(self,item):
		if self.count == self.length:
			print ("Overflow")
			return
		self.queue[self.rear] = item
		self.count= self.count+1
		self.rear = (self.rear+1)%self.length
	def dqueue(self):
		if self.count == 0:
			print ("-1")
			return
		self.queue[self.front] = 0;
		self.count = self.count+1
		self.front = (self.front+1)%self.length

q = CQueue(5)
q.dqueue()
q.enqueue(4)
print(q.queue)
q.enqueue(3)
q.enqueue(9)
q.enqueue(1)
q.enqueue(8)
q.enqueue(6)
print(q.queue)
q.dqueue()
q.enqueue(99)
print(q.queue)

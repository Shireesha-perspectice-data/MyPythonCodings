class stack:
	def __init__(self):  #creat a constructor
		self.items=[]     #instance variable
	def isEmpty(self):
		return self.items==[]
	def push(self):
		return self.items.append(element)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)

y=[11,22,33,12,14,14,15,16,20]
print(type(y))
print(y[0])
print(y[1])
y[1]=1432
print(y)

s=stack()
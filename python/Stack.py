class Stack(object):
	def _init_(self,size=10):
		self._content = []
		self._size = size
		self._current=0
	def empty(self):
		self._content=[]
		self._current=0
	def isEmpty(self):
		if not self._content:
			return True
		else:
			return False
	def setSize(self,size):
		if size <self._current:
			for i in range(size,self._current)[::-1]:
				del self._content[i]
			self._current = size
		self._size = size
	def isFull(self):
		if self._current==self._size:
			return True
		else:
			return False	


	def Push(self,v):
		if len(self._content)<self._size:
			self._content.append(v)
			self._current = self._current+1
		else:
			print('Stack Full!')

	def pop(self):
		if self._content:
			self._current = self._current-1
			return self._content.pop()
		else:
			print('Stack is empty!')


	def show(self):
		print(self._content)
	def showRemainderSpace(self):
		print('Stack can still PUSH',self._size-self._current,'elements')

if __name__=='__main__':
	print('Please use me as a module')
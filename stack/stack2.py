class Stack:
  def __init__(self, max):
    self.max = max
    self.stack = [None] * max
    self.top = -1

  def push(self, data):
    if(self.top == self.max - 1):
      print('Stack is already full!!')
    else:
      self.top = self.top + 1
      self.stack[self.top] = data
     
  def pop(self):
    if(self.top == -1):
      print('Stack is empty, there is nothing to pop()')
    else:
      self.stack[self.top] = None
      self.top = self.top - 1

  def printStack(self):
    if(self.top == -1):
      print('The stack is empty!!')
    else:
      print(self.stack)

stack = Stack(5)
stack.push(2)
stack.push(10)
stack.push(20)
stack.push(50)
stack.push(90)
stack.pop()
stack.printStack()
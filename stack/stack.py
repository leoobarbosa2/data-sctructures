maximum = 4

def create_stack():
  stack = []
  return stack

def check_is_empty(stack: list):
  return len(stack) == 0

def check_is_full(stack: list):
    return len(stack) == maximum

def push(stack: list, item: int):
  if(check_is_full(stack)):
      print('Stack is already full!')
  else:
    stack.append(item)
    print(f'pushed item {item}')

def pop(stack: list):
  if(len(stack)) == 0:
    print('Stack is empty!')
  else:
    stack.pop()

stack = create_stack()
push(stack, 1)
push(stack, 3)
push(stack, 8)
push(stack, 7)
push(stack, 8)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
push(stack, 2)
print(stack)


class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self, value):
    new_node = Node(value)
    self.first = new_node
    self.lasat = new_node
    self.length = 1
  def enqueue(self,value):
    new_node = Node(value)

    if self.first is None:
      self.first = new_node
      self.last = new_node

    else:
      self.last.next = new_node
      self.last = new_node
      self.length +=1

  def dequeue(self)
class Node:
  def __init__(self, data, nxt=None):
    self.data = data
    self.next = nxt

class LList:
  def __init__(self, head):
    self.head = head

  def insert(self, data):
    newNode = Node(data, None)
    if(self.head):
      curr = self.head
      while(curr.next):
        curr = curr.next
      curr.next = newNode
    else:
      self.head = newNode

  def remove(self):
    curr = self.head
    prev = curr
    while curr.next != None:
      prev = curr
      curr = curr.next
    del curr
    prev.next = None


  def print(self):
    curr = self.head
    out = ""
    while(curr):
      out += str(curr.data)
      if curr.next != None:
        out += " -> "
      curr = curr.next
    print(out)




class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def printL(self):
    itr = self.head
    string = ''
    while itr:
      string += str(itr.data) + ' --> '
      itr = itr.next
    print(string)


if __name__ == '__main__':
    LinkedList1 = LinkedList()
    Node1 = Node(15)
    LinkedList1.head = Node1

    Node2 = Node(12)
    Node3 = Node(4)

    Node1.next = Node2
    Node2.next = Node3

    LinkedList1.printL()


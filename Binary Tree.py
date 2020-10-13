class binaryTree:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
  
  def addChild(self,data):
    if self.left:
      if(self.right):
        self.left.addChild(data)
      else:
        self.right = binaryTree(data)

    else:
      self.left = binaryTree(data)

root = binaryTree(12)
root.addChild(13)
root.addChild(14)
root.addChild(16)
root.addChild(17)
print(root.left.right.data)
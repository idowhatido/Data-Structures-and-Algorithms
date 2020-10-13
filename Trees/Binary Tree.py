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

def buildTree(arr):
    root = binaryTree(arr[0])

    for i in range(1,len(arr)):
        root.addChild(arr[i])
    return(root)

if __name__ == '__main__':
    arr = [9,5,3,2,5,32,76,23,654,32]
    tree = buildTree(arr)
    print(tree.right.data)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
  
    def addNode(self,data):
        if(data == self.data):
            return
    
        if data < self.data:
            if(self.left):
                self.left.addNode(data)
            else:
                self.left = Node(data)
        else:
            if(self.right):
                self.right.addNode(data)
            else:
                self.right = Node(data)

def buildTree(arr):
    root = Node(arr[0])

    for i in range(1,len(arr)):
        root.addNode(arr[i])
    return(root)

if __name__ == '__main__':
    arr = [9,5,3,2,5,32,76,23,654,32]
    tree = buildTree(arr)
    print(tree.right.data)
# Linear Search or Sequential Search

def LinSer(arr,n):
  k = len(arr)
  for i in range(k):
    if(arr[i] == n):
      return(i)
  return(-1)
  
n = 5
arr = [234,523,64,73,865,95,1,9,23,41,4534,543,6,8,347457,4,52,5]
index = LinSer(arr,n)
if(index>=0):
  print("The element is at index : {}".format(index))
else:
  print("Element doesnt exist")
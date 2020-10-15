##BUBBLE SORT

def bubsort(arr):
  k = len(arr)
  for i in range(k-1):
    for j in range(k-i-1):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return(arr)

arra = ['B','U','B','B','L','E','S','O','R','T']
ans = bubsort(arra)
print(ans)
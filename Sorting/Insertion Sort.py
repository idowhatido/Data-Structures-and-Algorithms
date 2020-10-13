##INSERTION SORT

def insort(arr):
  k = len(arr)
  for i in range(1,k):
    j = i
    while(j>0 and (arr[j-1]>arr[j])):
      arr[j-1],arr[j] = arr[j],arr[j-1]
      j -= 1 
  return(arr)
  
arra = ['I','N','S','E','R','T','I','O','N','S','O','R','T']
ans = insort(arra)
print(ans)



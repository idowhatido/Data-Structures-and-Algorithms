##QUICKSORT

def partition(l,h):
  i = l
  j = h
  while(i<=j):
    while(arra[i]<=arra[l]):
      i+=1
    while(arra[j]>arra[l]):
      j-=1
    if(i<j):
      arra[i],arra[j] = arra[j],arra[i]
  arra[l],arra[j] = arra[j],arra[l]
  return(j)

def quicksort(l,h):
  if(l<h):
    part = partition(l,h)
    quicksort(l,part)
    quicksort(part+1,h)
  return(arra)

arra = [5,16,7,2,3,14,9,34]
k =len(arra)
ans = quicksort(0,k-1)
print(ans)

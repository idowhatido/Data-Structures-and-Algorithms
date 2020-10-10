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

#SELECTION SORT

def selsort(arr):
  k = len(arr)
  for i in range(k):
    mini = i
    for j in range(i,k):
      if(arr[j]<arr[mini]):
        mini = j
    arr[i],arr[mini] = arr[mini],arr[j]
  return(arr)

arra = ['S','E','L','E','C','T','I','O','N','S','O','R','T']
ans = selsort(arra)
print(ans)

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

##MERGESORT

def merge(l,mid,r):
  L = arra[l:mid+1]
  R = arra[mid+1:r+1]
  L.append(9999999)
  R.append(9999999)
  i = j = 0
  for k in range(l,r+1):
    if(L[i]<=R[j]):
      arra[k] = L[i]
      i+=1
    else:
      arra[k] = R[j]
      j+=1

def mergesort(l,r):
  if(l<r):
    mid = (l+r)//2
    mergesort(l,mid)
    mergesort(mid+1,r)
    merge(l,mid,r)

arra = [5,16,7,2,3,14,9,34]
k =len(arra)
mergesort(0,k-1)
print(arra)
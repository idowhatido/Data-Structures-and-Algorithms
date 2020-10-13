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
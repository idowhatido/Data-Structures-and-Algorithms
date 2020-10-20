def Binser(left,right,element,arr):
  middle = (left + right)//2    #Splitting the array into two halves
  if(element > arr[middle]):
    return(Binser(middle+1,right,element,arr))
  elif(element < arr[middle]):
    return(Binser(left, middle-1, element, arr))
  else:
    return(middle)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19]  #Sorted Array is required
pos = Binser(0,len(arr)-1,19,arr)
print('index : ' + str(pos))

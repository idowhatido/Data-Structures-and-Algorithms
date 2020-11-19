class Main
{
    static int majorityElement(int a[], int size)
    {
        if(size==1){
            return(a[0]);
        }
        int count = 1;
        int majority = 0;
        for(int i= 1;i<size;i++){
            if(a[majority]==a[i]){
                count++;}
            else{
                count--;
            }
            
            if(count==0){
                majority = i;
                count = 1;
            }
        }
     //   System.out.print(a[majority]);
        int counter = 0;
        for(int i = 0; i<size;i++){
            if(a[i] == a[majority]){
              
                counter++;
            }
        }
        System.out.print(counter);
        if(counter>(size/2)){
            return(a[majority]);
        
        }
        else{
            return(-1);
        }
        
    }

    public static void main(String[] args){
      
      int[] arr = {3,1,3,3,2};
      int n = arr.length;
      System.out.print(majorityElement(arr,n));
    }
}
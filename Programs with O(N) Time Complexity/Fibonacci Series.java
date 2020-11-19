class Main {
  public static void main(String[] args) {
    int n = 8;
    int[] memory = new int[n+1];
    for(int i = 0 ; i<n;i++){
      System.out.print(fibb(i, memory)+ " ");
    }
  }
   static int fibb(int n, int [] memory){
     if(n <= 0){
       return(0);
     }
     else if(n == 1){
       return(1);
     }
     else if(memory[n] > 0){
       return(memory[n]);
     }
     memory[n] = fibb(n-1,memory) + fibb(n-2,memory);
     return(memory[n]);
    }
  }

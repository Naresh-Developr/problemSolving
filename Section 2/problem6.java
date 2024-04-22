//Sort an array of 0s , 1s and 2s 
class problem6{

    public static void main(String[] args) {
        int[] arr ={1,0,1,0,2,0,1,2};
        int n = arr.length;
        sort(arr,n);

        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }

    }

    private static void sort(int[] arr,int n) {
        int left = 0;
        int size = n-1;

        for(int i=0;i<n;){
            if(arr[i]==0){
                swap(arr,left,i);
                left++;
                i++;
            }
            else if(arr[i]==2){
                swap(arr,size,i);
                size--;
            }else{
                i++;
            }
        }        
    }

    private static void swap(int[] arr, int left, int i) {
        int temp = arr[left];
        arr[left] = arr[i];
        arr[i] = temp; 

    }
}
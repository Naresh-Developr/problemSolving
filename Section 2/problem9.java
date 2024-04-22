//Rotate the array by k
public class problem9 {

    public static void main(String[] args) {
        int arr[] = {1, 3, 5, 7, 9};

        shift(arr,2);
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]);   
        }
        System.out.println();    
    }


    private static void shift(int[] arr,int k) {
        int v=0;
        while(v<k){
            int last_element = arr[arr.length-1];
        //System.out.println(last_element);
        for(int i=arr.length-1;i>0;i--){
            arr[i] = arr[i-1];
        }
        arr[0] = last_element;
        v++;
        }
        

        
    }
    
}

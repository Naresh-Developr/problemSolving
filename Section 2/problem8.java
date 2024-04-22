//Rotate the array by 1
public class problem8 {

    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,7,8,9,0};

        shift(arr);
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]);   
        }
        System.out.println();
        //System.out.println(arr);
    }

    private static void shift(int[] arr) {
        int last_element = arr[arr.length-1];
        //System.out.println(last_element);
        for(int i=arr.length-1;i>0;i--){
            arr[i] = arr[i-1];
        }
        arr[0] = last_element;
    }
    
}

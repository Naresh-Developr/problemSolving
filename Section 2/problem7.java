//Check if two arrays are equal or not

import java.util.Arrays;

public class problem7 {
    public static void main(String[] args) {
        int arr1[] = {1,2,3,4,5,6};
        int arr2[] = {1,2,3,4,5,6,7};

        boolean t = compare(arr1,arr2);

        if(t){
            System.out.println("Same array");
        }else{
            System.out.println("Different array");
        }
    }

    private static boolean compare(int[] arr1, int[] arr2) {
        int m = arr1.length;
        int n = arr2.length;

        if(m!=n) return false;

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        for(int i=0;i<m;i++){
                if(arr1[i] != arr2[i]){
                    return false;
            }
        }
        return true;

    }

    
}

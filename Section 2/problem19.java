import java.util.*;

public class problem19 {

    static long kthElement( int arr1[], int arr2[], int n, int m, int k) {
        
        int tS = n+m;
        
        int[] newArr = new int[tS];
        
        System.arraycopy(arr1,0,newArr,0,n);
        System.arraycopy(arr2,0,newArr,n,m);
    
        Arrays.sort(newArr);
        //System.out.println(Arrays.toString(newArr));
        
        return newArr[k-1];
        
    }

    public static void main(String[] args) {
        int[] arr1 = {2,3,4,5,6};
        int[] arr2 = {7,8,9,0,1};

        System.out.println(kthElement(arr1,arr2,5,5,5));
    }
    
}

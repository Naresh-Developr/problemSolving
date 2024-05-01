/**
 * problem16
 * Given an array Arr consisting of N distinct integers. The task is to 
 * count all the triplets such that sum of two elements equals the third element.
 */
import java.util.Arrays;
public class problem16 {

    static int count_Triplets(int[] arr,int n){
        Arrays.sort(arr);
        int count =0;

        for(int i=0;i<arr.length-1;i++){
            for(int j=i+1;j<arr.length;j++){
                int tot = arr[i]+arr[j];
                if(search(arr,tot)){
                    count+=1;
                }
            }
        }
        return count;
    }
    static boolean search(int[] arr,int n){
        int start = 1;
        int end = arr.length-1;
        while(start<=end){
            int mid = (start+end)/2;
            if(arr[mid]==n){
                return true;
            }else if(arr[mid]<n){
                start = mid+1;
            }else{
                end = mid-1;
            }
        } 
        return false;

    }

    public static void main(String[] args) {
        int[] arr = {1,5,3,2};
        System.out.println(count_Triplets(arr, 4));
    }
}


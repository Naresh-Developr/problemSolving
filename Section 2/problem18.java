/*
 * 
 * 
 */
import java.util.Arrays;
public class problem18 {
    public static int NumberofElementsInIntersection(int a[], int b[], int n, int m) {
        int count=0;
        Arrays.sort(a);
        Arrays.sort(b);

        
        if(n>m){
            //count = n;
        
        for(int i=0;i<m;i++){
            if(search(a,b[i])){
                count +=1;
            }
            else{
                continue;
            }
        }
        }
        else{
            //count = m;
            for(int i=0;i<n;i++){
            if(search(b,a[i])){
                count +=1;
            }
            else{
                continue;
            }
        }
        }
        
        return count;
    }
    
    static boolean search(int[] arr,int n){
        int start=0;
        int end = arr.length-1;
        
        while(start<=end){
            int mid = (start)+(end-start)/2;
            if(arr[mid]==n){
                return true;
            }else if(arr[mid]>n){
                end = mid-1;
            }else{
                start = mid+1;
            }
        }
        return false;
        
    }
    public static void main(String[] args) {
        int[] arr = {89,24,75,11,23};
        int[] arr1 = {89,2,4};

        System.out.println(NumberofElementsInIntersection(arr,arr1,5, 3));
    }
}

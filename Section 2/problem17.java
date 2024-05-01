//import java.util.Scanner;
public class problem17 {
    public static int doUnion(int a[], int n, int b[], int m) 
    {
        int count=0;
        
        if(n>m){
            count = n;
        
        for(int i=0;i<m;i++){
            if(search(a,b[i])){
                continue;
            }
            else{
                count +=1;
            }
        }
        }
        else{
            count = m;
            for(int i=0;i<n;i++){
            if(search(b,a[i])){
                continue;
            }
            else{
                count +=1;
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
        int[] arr = {1,2,3,4,5};
        int[] arr1 = {1,2};

        System.out.println(doUnion(arr, 5, arr1, 2));
    }
}

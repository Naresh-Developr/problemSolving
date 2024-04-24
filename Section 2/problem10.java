//Array subset of another array
public class problem10 {
    public static void main(String[] args) {
        int arr1[] = {1,2,3,4,5};
        int arr2[] = {5,4,3,1,2,6};

        if(subset(arr1,arr2)){
            System.out.println("Subset");

        }else{
            System.out.println("Not a subset");
        }
    }

    static boolean subset(int[] arr1, int[] arr2) {
        int m = arr1.length;
        int n = arr2.length;
        int i,j = 0;
        int count=0;

        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                if(arr1[i]==arr2[j]){
                    count++;
                }
                
            }
        }  
        if(count==arr1.length){
            return true;
        }
        else{
            return false;
        }  

        }
    }
    



class problem1{

    public static boolean searchMatrix(int[][] matrix, int k) {
        int n = matrix.length;
        int m = matrix[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
              if (k == matrix[i][j]) {
                return true;
                
              }
              
            }
          }
        return false;
    }

    public static void main(String[] args) {
        int[][] arr = {{1,3,5,7},
                    {10,11,16,20},
                    {23,30,34,60}
                };

        System.out.println(searchMatrix(arr,11));
    }


}
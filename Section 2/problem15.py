def findTriplets(arr, n):
        arr.sort()
        
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while(l<r):
                sum = arr[i]+arr[l]+arr[r]
                
                if(sum==0):
                    return 1
                elif(sum<0):
                    l+=1
                else:
                    r-=1
        return 0

arr =[1,2,3,4,5,6,7,8,9]
findTriplets(arr,9)
inv_count = 0
def sort(arr):
        global inv_count
        
        if len(arr)>1:
            mid = len(arr)//2
            L =arr[:mid]
            R =arr[mid:]
            sort(L)
            sort(R)
            merge(L,R,arr)
            
def merge(L,R,arr):
        i=j=k=0
        global inv_count
        while len(L)>i and len(R)>j:
            if(L[i]<R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
                inv_count[0] += len(L)-1
            k+=1
            
            
            while i<len(L):
                arr[k] = L[i]
                k+=1
                i+=1
                
            while j<len(R):
                arr[k] = L[j]
                k+=1
                j+=1
                
def inversionCount(arr):
        # Your Code Here
        global inv_count
        #inv_count = [0]
        
        sort(arr)
        
        print(inv_count)

arr = [2 ,4 ,1 ,3 ,5]

inversionCount(arr)
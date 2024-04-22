#Search an element in array
#Approches
#1. linear search
#2. Binary search

#2.

arr =  [1,2,3,4,5,7,7,9,9]

def binarySearch(arr,target,start,end):
    
    while start<=end :
        mid = start+(start-end)//2
        if(target>arr[mid]):
            start = mid+1
        elif(target<arr[mid]):
            end = mid-1
        else:
            return arr[mid]
        
print(binarySearch(arr,7,0,len(arr)-1))


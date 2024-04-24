#Find pair with given sum [Two sum]

def twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            if(arr[i]+arr[j] == target):
                return True
            
    return False

arr = [1,2,3,4,5]
if(twosum(arr,9)):
    print("true")
else:
    print("false")
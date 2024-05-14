	# Function to find maximum
	# product subarray
def maxProduct(arr):
    	# code here
		
	ans = arr[0]
		
	for i in range(len(arr)):
		temp = arr[i]
		for j in range(i+1,len(arr)):
			ans = max(ans,temp)
			temp *= arr[j]
        ans = max(ans,temp)
		    
	return ans

arr =  [1,2,4,5,3]

print(maxProduct(arr))
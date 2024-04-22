#Find missing number in array

# Function to get the missing number
def getMissingNo(a, n):
    for i in range(n):
        i+=i
    n = n*(n+1)//2 #formula

    return n-i


# Driver Code
if __name__ == '__main__':
    arr = [1,3,4,5]
    N = len(arr)

    # Function call
    print(getMissingNo(arr, N))

# This code is contributed by Mohit kumar

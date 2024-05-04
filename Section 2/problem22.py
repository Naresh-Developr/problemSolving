def maxSubArraySum(arr,N):
    n = -9999999
    first = 0

    for i in range(N):
        first = first+arr[i]

        if(n<first):
            n = first
        if(first<0):
            first = 0

    return n


arr = [1,2,3,-2,5]

print(maxSubArraySum(arr,5))
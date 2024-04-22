#Find third largest element in array
#approach 1
arr = [1,11,2,16,20,10]

def findThirdLargest(arr):
    first = arr[0]
    sec = 0
    third = 0

    for i in range(1,len(arr)-1):

        if(arr[i]>first):
            third = sec
            sec = first
            first = arr[i]
        elif(arr[i]>sec):
            third = sec
            sec = arr[i]
        elif(arr[i]>third):
            third = arr[i]

    return third

print(findThirdLargest(arr))

#arrpoach 2

#arr.sort()
#return arr[-3]

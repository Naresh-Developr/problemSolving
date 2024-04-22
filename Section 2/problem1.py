#Find the maximum and minimum element in array

#To find min and max faster is to sort the array first, so use merge sort
#approach 1
arr = [3, 5, 4, 1, 9]

def Split(arr, start,end):
    if(len(arr)>1):
        start = 0
        end = len(arr)-1
        #mid = len(arr)//2
        mid = start+(start-end)//2
        R = arr[mid:]
        L = arr[:mid]
        Split(L,start,end)
        Split(R,start,end)
        merge(L,R,arr)


def merge(l,r,arr):
    i=0
    j=0
    k=0

    while i<len(l) and j<len(r):
        if(l[i]<r[j]):
            arr[k] = l[i]
            i = i+1
        else:
            arr[k] = r[j]
            j = j+1
        k=k+1

    while i<len(l):
        arr[k] = l[i]
        i = i+1
        k = k+1

    while j<len(r):
        arr[k] = r[j]
        j+=1
        k+=1

Split(arr,0,len(arr)-1)
print("After split: ")
for i in range(len(arr)):
    print(arr[i])

print(f"{arr[0],arr[len(arr)-1]}")

#approach 2:

# arr.sort()
# return arr[0], arr[len(arr)-1]
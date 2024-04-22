#Find repeating number in array

arr = [1,3,2,3,1,2]
def findRepeating(arr):
    rp_elements = []
    for i in range(len(arr)):
        if arr[i] in rp_elements:
            continue
        for j in range(i+1,len(arr)):
            if(arr[i] == arr[j]):
                rp_elements.append(arr[i])
                break
    return rp_elements


print(findRepeating(arr))

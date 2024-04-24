#count frequency  od elements in aarray

arr = [1,1,2,3,1,3,2,2,3]

def count_freq(arr):
    dic = dict()

    for i in range(len(arr)):
        if arr[i] in dic.keys():
            dic[arr[i]]+=1
        else:
            dic[arr[i]] = 1

    for x in dic:
        print(x,dic[x])

count_freq(arr)

#approach 2:

def countFreq(arr):
    visited = [False for i in range(len(arr))]

    for i in range(len(arr)):
        if(visited[i]==True):
            continue

        count = 1

        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                count+=1
                visited[j]=True
        
        print(arr[i],count)
            
countFreq(arr)


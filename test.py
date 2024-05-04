# # 

# #4 sum
# def checkUnique(arr):
#         for i in range(len(arr)-1):
#             for j in range(i+1,len(arr)):
#                 if(arr[i]==arr[j]):
#                     return False
#         return True

# def FourSum(nums,target):
#         nums.sort()
#         n = len(nums)
#         ans =[]

#         for i in range(n):
#                 if(i>0 and nums[i]==nums[i-1]):
#                         continue
#                 for j in range(i+1,n):
#                         if(j>i+1 and nums[j]==nums[j-1]):
#                                 continue
                        
#                         k=j+1
#                         l = n-1

#                         while k<l:
#                                 sum = nums[i]+nums[j]+nums[k]+nums[l]
#                                 if sum == target:
#                                         temp = [nums[i],nums[j],nums[k],nums[l]]
#                                         if (checkUnique(temp)):      
#                                             ans.append(temp)
#                                             k +=1
#                                             l -=1
#                                             while(k<l and nums[k]==nums[k-1]):
#                                                     k+=1
#                                             while(k<l and nums[l]==nums[l-1]):
#                                                     l-=1
#                                         else:
#                                                 k +=1
#                                                 l -=1
#                                                 while(k<l and nums[k]==nums[k-1]):
#                                                         k+=1
#                                                 while(k<l and nums[l]==nums[l-1]):
#                                                         l-=1

#                                 elif(sum>target):
#                                         l-=1
#                                 else:
#                                         k+=1

#         return ans    
                                        
                                         
                        



# arr = [-1,0,-5,-2,-2,-4,0,1,-2]

# print(FourSum(arr,-9))
#inv_count = 0
def sort(arr):
    global inv_count
    if len(arr) >1 :
        mid = len(arr)//2
        R = arr[mid:]
        L = arr[:mid]
        sort(R)
        sort(L)
        merge(L,R,arr) 


def merge(l,r,arr):
    global inv_count
    i=0
    j=0
    k=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr[k] = l[i]
            i = i+1
        else:
            arr[k] = r[j]
            j = j+1
            inv_coun += len(l)-1
        k = k+1

    while i<len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    
    while j<len(r):
        arr[k] = r[j]
        j += 1 
        k += 1





if __name__ == '__main__':
    global inv_count
    inv_count = 0
    array = [7,6,5,4,3,2,1]
    print(f"Before: {array}")
    #test=[0,0,0,0,0,0,0]
    sort(array)
    print(f"After: {array}")
    print(inv_count)


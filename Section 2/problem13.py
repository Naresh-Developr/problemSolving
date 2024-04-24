#3 Sum
#bruteforce
def threeSum(arr,target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==target):
                    print(arr[i],arr[j],arr[k])
                    return True
                
    return False

arr = [1,2,3,4,5,6,7,8,9]
if(threeSum(arr,24)):
    print("true")
else:
    print("False")

#apprach 2
#optimized 
def threeSum(nums):
        nums.sort()
        result = []
        if(len(nums)<3):
            return []
        for i in range(len(nums)-2):
            if(nums[i]==nums[i-1] and i>0):
                continue
            a = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
                elif sum>0:
                    r-=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
                elif sum<0:
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return result
def majorityElement(nums):

        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]] +=1
            else:
                dict[nums[i]] =1

        for i in dict:
             print(dict.values())

        maxi = max(dict, key = lambda x: dict[x])
        
        return maxi

num = [3,3,4]

print(majorityElement(num))
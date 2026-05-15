def twoSum(self, nums, target):
    index_of = {}
    for i in range(len(nums)):
        value = nums[i]
        index_of[value] = i
    for i in range(len(nums)):
        value = nums[i]
        value2 = target - value
        if value2 in index_of:
            j = index_of[value2]    
            if i != j:
                return [i, j]
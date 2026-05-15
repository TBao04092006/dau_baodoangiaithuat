def thirdMax(self, nums):
        # Loại bỏ các số trùng lặp
        distinct_nums = sorted(list(set(nums)), reverse=True)
        
        if len(distinct_nums) >= 3:
            return distinct_nums[2]
        return distinct_nums[0]
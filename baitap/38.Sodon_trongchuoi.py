def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = res ^ n # Thực hiện phép XOR dồn dập
        return res
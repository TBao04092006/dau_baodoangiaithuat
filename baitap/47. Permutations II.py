def permuteUnique(self, nums):
        res = []
        nums.sort() # Sắp xếp để nhận diện số trùng lặp
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                # Bỏ qua nếu số hiện tại giống số trước đó và số trước chưa được dùng
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return res
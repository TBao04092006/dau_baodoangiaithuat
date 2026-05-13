def largestPerimeter(self, nums):
        # Sắp xếp mảng giảm dần
        nums.sort(reverse=True)
        
        # Duyệt qua các bộ ba cạnh liên tiếp
        for i in range(len(nums) - 2):
            # Kiểm tra bất đẳng thức tam giác: a + b > c
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        # Nếu không tìm thấy bộ ba nào thỏa mãn
        return 0
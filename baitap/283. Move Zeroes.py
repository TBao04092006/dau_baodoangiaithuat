def moveZeroes(nums):
        """
        Không trả về gì cả, chỉnh sửa nums trực tiếp (in-place).
        """
        last_non_zero_at = 0
        
        for cur in range(len(nums)):
            if nums[cur] != 0:
                # Hoán vị giá trị của phần tử hiện tại với vị trí trống cho số khác 0
                nums[last_non_zero_at], nums[cur] = nums[cur], nums[last_non_zero_at]
                last_non_zero_at += 1
        
def sortArrayByParity(nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Nếu bên trái lẻ và bên phải chẵn -> Hoán đổi
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            
            # Đẩy con trỏ left qua nếu đã là số chẵn
            if nums[left] % 2 == 0:
                left += 1
            # Đẩy con trỏ right lại nếu đã là số lẻ
            if nums[right] % 2 == 1:
                right -= 1
                
        return nums
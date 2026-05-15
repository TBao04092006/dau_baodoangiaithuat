def isMonotonic(nums):
        # Giả định ban đầu mảng thỏa mãn cả hai
        increasing = True
        decreasing = True
        
        for i in range(len(nums) - 1):
            # Nếu phần tử sau nhỏ hơn phần tử trước -> không thể là mảng tăng
            if nums[i] > nums[i+1]:
                increasing = False
            # Nếu phần tử sau lớn hơn phần tử trước -> không thể là mảng giảm
            if nums[i] < nums[i+1]:
                decreasing = False
                
        # Nếu mảng vẫn giữ được trạng thái tăng HOẶC giảm thì là đơn điệu
        return increasing or decreasing
        
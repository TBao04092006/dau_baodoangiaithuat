def triangleNumber(self, nums):
        # Sắp xếp mảng tăng dần
        nums.sort()
        n = len(nums)
        count = 0
        
        # Cố định cạnh lớn nhất là nums[i]
        # Chạy từ cuối mảng về đầu
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            
            while left < right:
                # Kiểm tra điều kiện: a + b > c
                if nums[left] + nums[right] > nums[i]:
                    # Nếu nums[left] + nums[right] > nums[i], thì
                    # tất cả các số từ left đến right-1 khi cộng với nums[right]
                    # cũng đều lớn hơn nums[i] (do mảng đã sắp xếp)
                    count += (right - left)
                    # Thu hẹp biên phải để kiểm tra cặp tiếp theo
                    right -= 1
                else:
                    # Nếu tổng quá nhỏ, tăng biên trái để tăng tổng
                    left += 1
                    
        return count
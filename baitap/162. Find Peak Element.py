def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                # Đang đi lên dốc, đỉnh nằm bên phải
                left = mid + 1
            else:
                # Đang đi xuống dốc, đỉnh nằm bên trái hoặc chính là mid
                right = mid
                
        return left
        
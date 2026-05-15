def missingNumber(nums):
        n = len(nums)
        # Tính tổng lý thuyết từ 0 đến n
        expected_sum = n * (n + 1) // 2
        # Tính tổng thực tế các phần tử trong mảng
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum
        
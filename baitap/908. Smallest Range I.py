def smallestRangeI(nums, k):
        # Bước 1: Tìm giá trị lớn nhất và nhỏ nhất hiện tại
        max_val = max(nums)
        min_val = min(nums)
        
        # Bước 2: Tính toán hiệu số sau khi đã tối ưu hóa bằng k
        # Hiệu số mới = (max_val - k) - (min_val + k) = max_val - min_val - 2*k
        result = max_val - min_val - 2 * k
        
        # Bước 3: Nếu kết quả dương, đó là khoảng cách nhỏ nhất. 
        # Nếu âm hoặc bằng 0, ta có thể đưa khoảng cách về 0.
        return max(0, result)
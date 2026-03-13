def findSubsequences(self, nums):
        res = []
        
        def backtrack(start, path):
            # Nếu dãy con có ít nhất 2 phần tử, thêm vào kết quả
            if len(path) >= 2:
                res.append(list(path))
            
            # Sử dụng một set để theo dõi các số đã dùng tại level này
            used_in_step = set()
            
            for i in range(start, len(nums)):
                # Kiểm tra 2 điều kiện:
                # 1. Số này chưa được dùng ở vị trí này (tránh trùng)
                # 2. Số này giúp duy trì dãy không giảm
                if nums[i] in used_in_step:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used_in_step.add(nums[i]) # Đánh dấu đã dùng
                    path.append(nums[i])      # Chọn số
                    backtrack(i + 1, path)    # Đệ quy cho số tiếp theo
                    path.pop()                # Quay lui (backtrack)
        
        backtrack(0, [])
        return res
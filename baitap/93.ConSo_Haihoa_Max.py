def findLHS(self, nums):
        # Bước 1: Đếm số lần xuất hiện của từng phần tử
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        max_length = 0
        
        # Bước 2: Duyệt qua các số trong bảng đếm
        for x in counts:
            # Kiểm tra xem có số x + 1 để tạo thành cặp hài hòa không
            if x + 1 in counts:
                # Độ dài = (số lượng x) + (số lượng x + 1)
                current_length = counts[x] + counts[x + 1]
                max_length = max(max_length, current_length)
                
        return max_length
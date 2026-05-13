def distributeCandies(candyType):
        # 1. Tính giới hạn số kẹo Alice được ăn (n / 2)
        limit = len(candyType) // 2
        
        # 2. Tìm số lượng các loại kẹo khác nhau bằng Set
        unique_candies = len(set(candyType))
        
        # 3. Kết quả là giá trị nhỏ nhất giữa số loại kẹo và giới hạn
        return min(unique_candies, limit)
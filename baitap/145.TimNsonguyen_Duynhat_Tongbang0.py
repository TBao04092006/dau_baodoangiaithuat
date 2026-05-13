def sumZero(self, n):
        res = []
        
        # Thêm các cặp số đối nhau (i và -i)
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
            
        # Nếu n lẻ, thêm số 0 để hoàn tất
        if n % 2 != 0:
            res.append(0)
            
        return res
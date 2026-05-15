def minimumTotal(self, triangle):
        # Lấy hàng cuối cùng làm hàng cơ sở để tính toán
        # Chúng ta dùng mảng một chiều để tiết kiệm bộ nhớ
        dp = triangle[-1]
        
        # Duyệt từ hàng kế cuối lên đến đỉnh (hàng 0)
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Giá trị tại nút hiện tại = chính nó + giá trị nhỏ nhất của 2 nút kề dưới
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        # Sau khi cộng dồn lên tới đỉnh, kết quả nằm ở vị trí đầu tiên
        return dp[0]
        
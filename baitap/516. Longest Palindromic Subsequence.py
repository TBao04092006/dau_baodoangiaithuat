def longestPalindromeSubseq(self, s):
        n = len(s)
        # Khởi tạo bảng dp n x n với tất cả giá trị là 0
        dp = [[0] * n for _ in range(n)]
        
        # Mọi ký tự đơn lẻ đều là một palindrome độ dài 1
        for i in range(n):
            dp[i][i] = 1
            
        # Duyệt qua các độ dài chuỗi con từ 2 đến n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # Nếu hai đầu giống nhau, cộng 2 vào kết quả của đoạn giữa
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # Nếu khác nhau, lấy giá trị lớn nhất khi bỏ đầu hoặc bỏ đuôi
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]
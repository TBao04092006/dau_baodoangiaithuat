def shortestToChar(s, c):
        n = len(s)
        ans = [0] * n
        
        # Vị trí của ký tự 'c' gần nhất vừa gặp
        # Khởi tạo bằng một số rất nhỏ để đại diện cho việc chưa thấy 'c'
        prev = float('-inf')
        
        # Lượt đi: Trái sang Phải
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
            
        # Lượt về: Phải sang Trái
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            # Lấy giá trị nhỏ hơn giữa lượt đi và khoảng cách mới tính được
            ans[i] = min(ans[i], prev - i)
            
        return ans
        
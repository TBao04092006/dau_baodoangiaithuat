def buddyStrings(s, goal):
        # Điều kiện tiên quyết: độ dài phải bằng nhau
        if len(s) != len(goal):
            return False
            
        # Trường hợp 2 chuỗi giống hệt nhau
        if s == goal:
            # Trả về True nếu có ký tự lặp lại (dùng set để kiểm tra)
            return len(set(s)) < len(s)
            
        # Trường hợp 2 chuỗi khác nhau: tìm các vị trí không khớp
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                
        # Phải có đúng 2 vị trí khác nhau và chéo nhau thì mới hoán đổi được
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
        
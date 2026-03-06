def firstUniqChar(self, s):
        # Bước 1: Đếm số lần xuất hiện của mỗi ký tự
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Bước 2: Tìm ký tự đầu tiên có tần suất là 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        # Bước 3: Không tìm thấy ký tự nào duy nhất
        return -1
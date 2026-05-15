def mostCommonWord(paragraph, banned):
        # 1. Chuyển về chữ thường và thay thế các dấu câu bằng khoảng trắng
        # Dùng regex [^\w] để tìm mọi ký tự không phải là chữ cái hoặc số
        normalized_str = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        
        # 2. Tách chuỗi thành danh sách các từ
        words = normalized_str.split()
        
        # 3. Chuyển banned thành một set để tra cứu nhanh hơn (O(1))
        banned_set = set(banned)
        
        # 4. Lọc các từ không bị cấm
        valid_words = [word for word in words if word not in banned_set]
        
        # 5. Đếm tần suất và trả về từ xuất hiện nhiều nhất
        counts = Counter(valid_words)
        return counts.most_common(1)[0][0]
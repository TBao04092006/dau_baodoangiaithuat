def commonChars(self, words):
        # Khởi tạo Counter với từ đầu tiên
        res = Counter(words[0])
        
        # Lấy giao điểm của Counter hiện tại với từng từ tiếp theo
        for i in range(1, len(words)):
            res &= Counter(words[i])
            
        # Trình bày kết quả dưới dạng danh sách các ký tự
        return list(res.elements())
        
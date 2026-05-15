def lengthOfLastWord(self, s):
        # strip() xóa khoảng trắng thừa ở đầu/cuối
        # split() tách chuỗi thành danh sách các từ
        words = s.strip().split()
        
        if not words:
            return 0
            
        return len(words[-1]) # Trả về độ dài từ cuối cùng
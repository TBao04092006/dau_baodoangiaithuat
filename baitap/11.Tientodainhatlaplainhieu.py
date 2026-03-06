def longestCommonPrefix(self, strs):
    # Nếu mảng rỗng, trả về chuỗi rỗng ngay lập tức
    if not strs:
        return ""
    
    # Lấy chuỗi đầu tiên làm "mốc" để so sánh
    first_word = strs[0]
    
    # Duyệt qua từng vị trí ký tự của chuỗi đầu tiên
    for i in range(len(first_word)):
        char = first_word[i]
        
        # So sánh ký tự này với các chuỗi còn lại trong mảng
        for other_word in strs[1:]:
            # Nếu đã duyệt hết một từ khác HOẶC ký tự không khớp
            if i == len(other_word) or other_word[i] != char:
                # Trả về phần đã khớp trước đó
                return first_word[:i]
                
    # Nếu duyệt hết chuỗi đầu tiên mà mọi thứ đều khớp
    return first_word
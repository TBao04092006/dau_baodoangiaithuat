def isValid(self, s):
        # Tạo bảng tra cứu dấu đóng - mở
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # Nếu là dấu đóng
            if char in mapping:
                # Lấy phần tử trên cùng của stack, nếu trống thì dùng '#'
                top_element = stack.pop() if stack else '#'
                
                # Nếu dấu mở lấy ra không khớp với dấu đóng hiện tại
                if mapping[char] != top_element:
                    return False
            else:
                # Nếu là dấu mở, đẩy vào stack
                stack.append(char)

        # Trả về True nếu stack rỗng (tất cả đã khớp), ngược lại False
        return not stack
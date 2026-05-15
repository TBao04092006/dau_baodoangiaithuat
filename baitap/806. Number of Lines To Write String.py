def numberOfLines(widths, s):
        # Bắt đầu với dòng thứ nhất
        lines = 1
        current_width = 0
        
        for char in s:
            # Tìm độ rộng của ký tự hiện tại (a -> index 0, b -> index 1, ...)
            w = widths[ord(char) - ord('a')]
            
            # Kiểm tra nếu thêm ký tự này vào dòng hiện tại có bị quá 100 không
            if current_width + w > 100:
                # Nếu quá, ký tự này sẽ nằm ở dòng mới
                lines += 1
                current_width = w
            else:
                # Nếu không, cộng dồn vào dòng hiện tại
                current_width += w
                
        return [lines, current_width]
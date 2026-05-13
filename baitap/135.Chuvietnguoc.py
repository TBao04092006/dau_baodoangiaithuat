def reverseOnlyLetters(self, s):
        # Chuyển chuỗi thành list để có thể thay đổi các phần tử
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Nếu bên trái không phải chữ cái, bỏ qua
            if not s_list[left].isalpha():
                left += 1
            # Nếu bên phải không phải chữ cái, bỏ qua
            elif not s_list[right].isalpha():
                right -= 1
            # Nếu cả hai đều là chữ cái, hoán đổi chúng
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return "".join(s_list)
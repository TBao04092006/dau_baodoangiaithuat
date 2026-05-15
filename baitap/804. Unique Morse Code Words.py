def uniqueMorseRepresentations(words):
        # Bảng mã Morse cho 26 chữ cái (từ 'a' đến 'z')
        morse_table = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        # Sử dụng Set để lưu trữ các phép biến đổi độc nhất
        seen_transformations = set()
        
        for word in words:
            transformation = []
            for char in word:
                # Tính chỉ số của chữ cái (a -> 0, b -> 1, ...)
                index = ord(char) - ord('a')
                transformation.append(morse_table[index])
            
            # Ghép các mã Morse thành một chuỗi duy nhất và thêm vào Set
            seen_transformations.add("".join(transformation))
            
        # Số lượng phần tử trong Set chính là kết quả cần tìm
        return len(seen_transformations)
def wordPattern(pattern, s):
        words = s.split()
        
        # Nếu số lượng ký tự và số lượng từ không bằng nhau thì không khớp
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Kiểm tra ánh xạ từ ký tự sang từ
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Kiểm tra ánh xạ từ từ sang ký tự (đảm bảo tính duy nhất)
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True
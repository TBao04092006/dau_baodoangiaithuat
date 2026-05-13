def toGoatLatin(sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        
        for i, word in enumerate(words):
            # Quy tắc 1 & 2: Kiểm tra nguyên âm hay phụ âm
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            
            # Quy tắc 3: Thêm các chữ cái 'a' dựa trên chỉ số index (bắt đầu từ 1)
            new_word += "a" * (i + 1)
            
            result.append(new_word)
            
        # Ghép các từ lại thành một câu hoàn chỉnh cách nhau bởi khoảng trắng
        return " ".join(result)
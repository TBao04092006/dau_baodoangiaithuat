def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_len = 0
        start = 0
        
        for end in range(len(s)):
            # Nếu ký tự đã xuất hiện, di chuyển start đến sau vị trí cũ của nó
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)
            
            char_map[s[end]] = end
            max_len = max(max_len, end - start + 1)
            
        return max_len
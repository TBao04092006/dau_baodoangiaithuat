def countSubstrings(self, s):
        def countFromCenter(left, right):
            count = 0
            # Mở rộng ra hai phía chừng nào còn đối xứng
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            # Trường hợp 1: Tâm là 1 ký tự (độ dài lẻ)
            total_palindromes += countFromCenter(i, i)
            # Trường hợp 2: Tâm là giữa 2 ký tự (độ dài chẵn)
            total_palindromes += countFromCenter(i, i + 1)
            
        return total_palindromes
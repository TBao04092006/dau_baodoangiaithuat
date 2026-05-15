def isPalindrome(x):
        # Nếu x âm hoặc x kết thúc bằng 0 (nhưng không phải là 0), không phải số đối xứng
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
print(isPalindrome(121))            
print(isPalindrome(-121))     
print(isPalindrome(10))     
print(isPalindrome(0))     
def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            # Hoán đổi giá trị tại hai đầu
            s[left], s[right] = s[right], s[left]
            # Thu hẹp khoảng cách
            left += 1
            right -= 1
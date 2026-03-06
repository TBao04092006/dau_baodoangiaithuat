def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i # Trừ dần cho các số lẻ 1, 3, 5, 7...
            i += 2
        return num == 0 # Nếu trừ vừa hết về 0 thì là số chính phương
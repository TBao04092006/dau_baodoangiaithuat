def integerReplacement(self, n):
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # Nếu n kết thúc bằng ..01, trừ 1 sẽ tốt hơn
                n -= 1
            else:
                # Nếu n kết thúc bằng ..11, cộng 1 sẽ tạo ra nhiều số 0 hơn
                n += 1
            steps += 1
        return steps
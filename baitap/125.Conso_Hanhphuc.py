def isHappy(n):
        # Hàm bổ trợ để tính tổng bình phương các chữ số
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        # Tiếp tục lặp nếu n chưa bằng 1 và chưa xuất hiện trong chu kỳ cũ
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            
        return n == 1
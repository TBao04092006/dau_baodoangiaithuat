def primePalindrome(n):
        def is_prime(num):
            if num < 2: return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Duyệt theo độ dài của số đối xứng (từ 1 đến 9 chữ số)
        for length in range(len(str(n)), 10):
            # Sinh số đối xứng từ nửa đầu
            # Ví dụ: nửa đầu '12' sinh ra '121' (lẻ) hoặc '1221' (chẵn)
            # Nhưng ta biết số đối xứng chẵn chữ số (>11) không phải số nguyên tố
            # Nên ta tập trung sinh số lẻ chữ số
            
            # Xử lý trường hợp đặc biệt số 11
            if length == 2:
                if n <= 11: return 11
                continue # Bỏ qua các số có 2 chữ số khác
            
            # Nếu length là chẵn và > 2, bỏ qua theo quy luật chia hết cho 11
            if length % 2 == 0:
                continue

            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            
            for i in range(start, end):
                s = str(i)
                # Tạo số đối xứng lẻ chữ số: '123' -> '123' + '21' -> '12321'
                palindrome = int(s + s[-2::-1])
                
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
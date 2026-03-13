def repeatedSubstringPattern(s):
    n = len(s)
    # Thử mọi độ dài chuỗi con i từ 1 đến n/2
    for i in range(1, n // 2 + 1):
        # Nếu n chia hết cho i
        if n % i == 0:
            substring = s[:i]
            # Kiểm tra xem nếu lặp lại chuỗi con này n/i lần thì có ra s không
            if substring * (n // i) == s:
                return True
    return False
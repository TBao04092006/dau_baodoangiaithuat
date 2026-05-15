def licenseKeyFormatting(s, k):
        # Bước 1: Loại bỏ dấu gạch ngang và in hoa toàn bộ
        clean_s = s.replace("-", "").upper()
        
        n = len(clean_s)
        res = []
        
        # Bước 2: Duyệt từ cuối chuỗi về đầu theo bước nhảy k
        # Chúng ta lấy các nhóm k ký tự từ phải sang trái
        for i in range(n, 0, -k):
            # Nếu i - k < 0, slice sẽ lấy từ 0 đến i (xử lý luôn nhóm đầu tiên bị lẻ)
            start = max(0, i - k)
            res.append(clean_s[start:i])
            
        # Bước 3: Đảo ngược danh sách các nhóm và nối chúng bằng dấu "-"
        # Vì chúng ta lấy từ cuối lên nên res đang chứa các nhóm theo thứ tự ngược
        return "-".join(res[::-1])
        
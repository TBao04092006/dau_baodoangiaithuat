def binaryGap(n):
        # Chuyển số n thành chuỗi nhị phân (ví dụ: "10110")
        binary = bin(n)[2:]
        
        max_dist = 0
        last_pos = -1 # Lưu vị trí của bit 1 gần nhất
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_pos != -1:
                    # Tính khoảng cách giữa 2 bit 1 liền kề
                    max_dist = max(max_dist, i - last_pos)
                # Cập nhật vị trí bit 1 hiện tại
                last_pos = i
                
        return max_dist
        
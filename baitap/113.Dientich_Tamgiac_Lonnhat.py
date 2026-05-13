def largestTriangleArea(points):
        max_area = 0
        n = len(points)
        
        # Duyệt qua tất cả các tổ hợp 3 điểm khác nhau (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Lấy tọa độ của 3 điểm
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    
                    # Áp dụng công thức Shoelace
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    
                    # Cập nhật diện tích lớn nhất
                    if area > max_area:
                        max_area = area
                        
        return max_area
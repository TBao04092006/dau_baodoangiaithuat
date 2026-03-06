def generate(self, numRows):
        # Khởi tạo danh sách kết quả
        res = []
        
        for i in range(numRows):
            # Tạo một dòng mới toàn số 1 với độ dài (i + 1)
            row = [1] * (i + 1)
            
            # Cập nhật các giá trị ở giữa dòng (nếu có)
            for j in range(1, i):
                # Giá trị = (số cùng cột dòng trước) + (số cột trước dòng trước)
                row[j] = res[i-1][j-1] + res[i-1][j]
            
            # Thêm dòng vừa tạo vào kết quả
            res.append(row)
            
        return res
        
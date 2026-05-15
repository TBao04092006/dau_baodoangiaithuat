def getRow(self, rowIndex):
        # Khởi tạo dòng đầu tiên là [1]
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Thêm số 1 vào cuối mỗi dòng mới
            row.append(1)
            # Cập nhật các số ở giữa từ phải sang trái
            # (Để không làm hỏng giá trị cũ của dòng trước đó)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j-1]
                
        return row
def maxDepth(root):
        # Trường hợp cơ bản: Nếu cây rỗng (root là None)
        if not root:
            return 0
        
        # Nếu nút hiện tại không có con, độ sâu là 1
        if not root.children:
            return 1
        
        # Đệ quy tìm độ sâu của tất cả các nhánh con
        depths = [maxDepth(child) for child in root.children]
        
        # Kết quả là độ sâu lớn nhất của các con cộng thêm 1 (chính nút hiện tại)
        return max(depths) + 1
        
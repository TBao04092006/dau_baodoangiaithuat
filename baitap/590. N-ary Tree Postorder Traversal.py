def postorder(root):
        # Nếu cây trống, trả về danh sách rỗng
        if not root:
            return []
        
        res = []
        
        # 1. Duyệt qua từng nút con trước (Đệ quy)
        for child in root.children:
            res.extend(postorder(child))
            
        # 2. Sau khi xong hết các con, mới thêm giá trị của nút gốc vào cuối
        res.append(root.val)
        
        return res
        
def preorder(root):
        if not root:
            return []
        
        res = []
        
        # 1. Thăm nút gốc
        res.append(root.val)
        
        # 2. Duyệt qua từng nút con và thực hiện lại quá trình (đệ quy)
        for child in root.children:
            # Cộng thêm danh sách kết quả từ các nhánh con
            res.extend(preorder(child))
            
        return res
        
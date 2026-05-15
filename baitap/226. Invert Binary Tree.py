def invertTree(self, root):
        # 1. Điều kiện dừng: Nếu nút rỗng thì trả về None
        if not root:
            return None
        
        # 2. Hoán đổi hai con của nút hiện tại
        root.left, root.right = root.right, root.left
        
        # 3. Tiếp tục thực hiện tương tự với các nhánh con
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. Trả về gốc của cây đã đảo ngược
        return root
        
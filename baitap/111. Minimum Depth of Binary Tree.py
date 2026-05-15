def minDepth(self, root):
        if not root: 
            return 0
        
        # Nếu là nút lá (không có con trái và phải)
        if not root.left and not root.right:
            return 1
        
        # Nếu nhánh trái trống, phải tìm bên nhánh phải
        if not root.left:
            return 1 + self.minDepth(root.right)
            
        # Nếu nhánh phải trống, phải tìm bên nhánh trái
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Nếu có cả hai nhánh, lấy giá trị nhỏ nhất
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
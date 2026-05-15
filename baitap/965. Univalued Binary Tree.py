def isUnivalTree(self, root):
        if not root:
            return True
        
        # Kiểm tra nhánh trái
        if root.left and root.left.val != root.val:
            return False
            
        # Kiểm tra nhánh phải
        if root.right and root.right.val != root.val:
            return False
            
        # Đệ quy xuống các tầng thấp hơn
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
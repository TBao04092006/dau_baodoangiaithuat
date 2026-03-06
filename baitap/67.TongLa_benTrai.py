def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        total = 0
        # Kiểm tra nếu con bên trái tồn tại và là một nút lá
        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        
        # Tiếp tục duyệt sang bên phải
        total += self.sumOfLeftLeaves(root.right)
        
        return total
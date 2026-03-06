def hasPathSum(self, root, targetSum):
        # 1. Nếu cây rỗng, không bao giờ có đường đi
        if not root:
            return False
        
        # 2. Cập nhật targetSum bằng cách trừ đi giá trị nút hiện tại
        targetSum -= root.val
        
        # 3. Kiểm tra nếu đây là nút lá
        if not root.left and not root.right:
            return targetSum == 0
        
        # 4. Đệ quy xuống nhánh trái HOẶC nhánh phải
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
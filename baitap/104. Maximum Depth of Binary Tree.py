def maxDepth(self, root):
        # Nếu cây rỗng, độ sâu bằng 0
        if not root:
            return 0
        
        # Độ sâu = 1 + giá trị lớn nhất giữa nhánh trái và nhánh phải
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
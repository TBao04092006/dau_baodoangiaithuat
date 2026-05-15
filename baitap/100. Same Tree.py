def isSameTree(self, p, q):
        # Nếu cả hai đều rỗng thì giống nhau
        if not p and not q:
            return True
        # Nếu một cái rỗng, một cái có hoặc giá trị khác nhau thì sai
        if not p or not q or p.val != q.val:
            return False
        
        # Tiếp tục so sánh đệ quy nhánh trái và nhánh phải
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
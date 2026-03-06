def isSymmetric(self, root):
        def check(left, right):
            # Nếu cả hai nhánh đều rỗng -> đối xứng
            if not left and not right:
                return True
            # Nếu chỉ một bên rỗng hoặc giá trị khác nhau -> không đối xứng
            if not left or not right or left.val != right.val:
                return False
            # So sánh chéo: trái của nhánh trái với phải của nhánh phải...
            return check(left.left, right.right) and check(left.right, right.left)
        
        return check(root.left, root.right) if root else True
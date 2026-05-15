def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def countNodes(self, root):
        # Nếu cây trống, trả về 0
        if not root:
            return 0
        
        # Đệ quy: 1 (nút hiện tại) + con bên trái + con bên phải
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
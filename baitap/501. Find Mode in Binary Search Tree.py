def findMode(self, root):
        self.max_count = 0
        self.current_count = 0
        self.prev = None
        self.res = []

        def inOrder(node):
            if not node: return
            
            inOrder(node.left)
            
            # Xử lý node hiện tại
            if node.val == self.prev:
                self.current_count += 1
            else:
                self.current_count = 1
            
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.res = [node.val]
            elif self.current_count == self.max_count:
                self.res.append(node.val)
            
            self.prev = node.val
            
            inOrder(node.right)

        inOrder(root)
        return self.res
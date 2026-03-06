def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head) # type: ignore
        slow = fast = dummy
        
        # Fast đi trước n bước
        for _ in range(n):
            fast = fast.next
            
        # Cả hai cùng đi cho đến khi fast chạm cuối
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # Xóa nút
        slow.next = slow.next.next
        return dummy.next
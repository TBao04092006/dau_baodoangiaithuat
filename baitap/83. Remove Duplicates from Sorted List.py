def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next # Xóa nút trùng
            else:
                curr = curr.next # Tiến lên nút tiếp theo
        return head
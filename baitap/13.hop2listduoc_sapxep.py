def mergeTwoLists(self, list1, list2):
        # Tạo một nút giả để bắt đầu danh sách mới
        dummy = ListNode(0) # type: ignore
        current = dummy

        # Duyệt khi cả hai danh sách đều còn phần tử
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Nếu một trong hai danh sách hết trước, nối phần còn lại của danh sách kia vào
        current.next = list1 if list1 else list2

        # Trả về nút bắt đầu thực sự (sau nút giả)
        return dummy.next
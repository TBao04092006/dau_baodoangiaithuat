def removeElement(self, nums, val):
        # k là con trỏ dùng để ghi đè các giá trị hợp lệ
        k = 0
        
        # Duyệt qua từng phần tử trong mảng
        for i in range(len(nums)):
            # Nếu phần tử hiện tại khác với giá trị cần xóa (val)
            if nums[i] != val:
                # Ghi giá trị đó vào vị trí của con trỏ k
                nums[k] = nums[i]
                # Tăng k lên để chuẩn bị cho phần tử tiếp theo
                k += 1
        
        # k chính là số lượng phần tử không bằng val
        return k
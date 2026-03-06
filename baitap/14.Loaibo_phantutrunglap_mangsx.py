def removeDuplicates(self, nums):
        # Nếu mảng rỗng, trả về 0
        if not nums:
            return 0
        
        # k là con trỏ đại diện cho vị trí phần tử duy nhất
        k = 1 
        
        # Duyệt từ phần tử thứ 2 đến hết mảng
        for i in range(1, len(nums)):
            # Nếu phần tử hiện tại khác với phần tử duy nhất trước đó
            if nums[i] != nums[i - 1]:
                # Ghi đè phần tử hiện tại vào vị trí k
                nums[k] = nums[i]
                # Tăng k lên 1
                k += 1
        
        # Trả về số lượng phần tử duy nhất
        return k
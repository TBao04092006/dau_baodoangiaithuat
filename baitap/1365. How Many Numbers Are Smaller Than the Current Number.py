def smallerNumbersThanCurrent(self, nums):
        result = []
        # Duyệt qua từng số trong mảng (số hiện tại)
        for i in range(len(nums)):
            count = 0
            # So sánh số hiện tại với tất cả các số khác
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            # Thêm kết quả đếm được vào danh sách kết quả
            result.append(count)
        return result
        
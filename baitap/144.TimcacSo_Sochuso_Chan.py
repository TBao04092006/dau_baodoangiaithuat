def findNumbers(self, nums):
        count = 0
        for n in nums:
            # Chuyển số n thành chuỗi và kiểm tra độ dài
            if len(str(n)) % 2 == 0:
                count += 1
        return count
        
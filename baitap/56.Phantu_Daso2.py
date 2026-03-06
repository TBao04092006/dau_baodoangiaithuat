from collections import Counter
def majorityElement(self, nums):
        # Bước 1: Đếm tần suất xuất hiện của mỗi số
        counts = Counter(nums)
        n = len(nums)
        
        # Bước 2: Lọc ra các số có tần suất > n/3
        result = []
        for num, count in counts.items():
            if count > n // 3:
                result.append(num)
        
        return result
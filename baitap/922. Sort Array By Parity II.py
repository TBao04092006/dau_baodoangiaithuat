def sortArrayByParityII(self, nums):
        n = len(nums)
        odd = 1
        
        # Duyệt qua các chỉ số chẵn
        for even in range(0, n, 2):
            # Nếu tại chỉ số chẵn mà gặp số lẻ
            if nums[even] % 2 != 0:
                # Tìm chỉ số lẻ nào đang chứa số chẵn
                while nums[odd] % 2 != 0:
                    odd += 2
                
                # Hoán đổi để đưa cả hai về đúng vị trí
                nums[even], nums[odd] = nums[odd], nums[even]
                
        return nums
        
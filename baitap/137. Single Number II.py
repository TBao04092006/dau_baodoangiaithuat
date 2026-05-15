def singleNumber(self, nums):
        ans = 0
        # Xét qua 32 vị trí bit
        for i in range(32):
            bit_count = 0
            for n in nums:
                # Kiểm tra bit thứ i của số n có phải là 1 không
                if (n >> i) & 1:
                    bit_count += 1
            
            # Nếu số lượng bit 1 không chia hết cho 3, 
            # thì bit thứ i này thuộc về số cần tìm
            if bit_count % 3 != 0:
                # Xử lý riêng cho số âm trong Python (do Python dùng số nguyên vô hạn)
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
def countBits(self, n):
        # Khởi tạo mảng kết quả với toàn số 0
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ans[i] = ans[i // 2] + (1 nếu i lẻ, 0 nếu i chẵn)
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
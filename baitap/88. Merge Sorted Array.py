def merge(self, nums1, m, nums2, n):
        # Ba vị trí con trỏ:
        i = m - 1      # Cuối phần tử thực của nums1
        j = n - 1      # Cuối của nums2
        k = m + n - 1  # Cuối cùng của mảng nums1 (tổng độ dài)

        # Duyệt khi nums2 vẫn còn phần tử
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
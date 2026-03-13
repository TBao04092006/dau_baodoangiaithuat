def searchRange(self, nums, target):
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # Nếu tìm vị trí đầu, tiếp tục thu hẹp về bên trái
                        right = mid - 1
                    else:
                        # Nếu tìm vị trí cuối, tiếp tục thu hẹp về bên phải
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [findBound(True), findBound(False)]
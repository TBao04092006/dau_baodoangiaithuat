def checkIfExist(self, arr):
        n = len(arr)
        # Duyệt qua từng phần tử i
        for i in range(n):
            # Duyệt qua từng phần tử j để so sánh với i
            for j in range(n):
                # Điều kiện: i khác j VÀ số này gấp đôi số kia
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
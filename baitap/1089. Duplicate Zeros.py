def duplicateZeros(self, arr):
        possible_dups = 0
        length = len(arr) - 1

        # Bước 1: Tìm phạm vi các phần tử sẽ còn sót lại trong mảng mới
        for i in range(length + 1):
            if i > length - possible_dups:
                break
            if arr[i] == 0:
                # Trường hợp đặc biệt: số 0 nằm ngay sát mép mảng không thể nhân đôi
                if i == length - possible_dups:
                    arr[length] = 0
                    length -= 1
                    break
                possible_dups += 1

        # Bước 2: Duyệt ngược để dịch chuyển và nhân đôi
        last = length - possible_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
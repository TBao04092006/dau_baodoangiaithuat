def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                # Nếu là số chẵn, chia cho 2
                num //= 2
            else:
                # Nếu là số lẻ, trừ đi 1
                num -= 1
            steps += 1
        return steps
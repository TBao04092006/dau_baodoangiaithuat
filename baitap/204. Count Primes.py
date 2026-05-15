def countPrimes(self, n):
        if n < 3:
            return 0
        
        # Giả định tất cả là số nguyên tố (True)
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                # Đánh dấu các bội số của i là False
                for j in range(i * i, n, i):
                    primes[j] = False
                    
        return sum(primes)
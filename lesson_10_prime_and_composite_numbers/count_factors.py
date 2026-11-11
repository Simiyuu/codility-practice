def solution(N):
    factors = 0
    i = 1

    # Symmetric divisor pairing: iterate only up to sqrt(N)
    while i * i < N:
        if N % i == 0:
            factors += 2 # Pair (i, N // i)
        i += 1

        # Check if N is a perfect square
        if i * i == N:
            factors += 1

        return factors
    
if __name__ == "__main__":
    print(solution(24)) # Expected output: 8 (1, 2, 3, 4, 6, 8, 12, 24)
    print(solution(16)) # Expected output: 5 (1, 2, 4, 8, 16)

    
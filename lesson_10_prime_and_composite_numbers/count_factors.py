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
    test_cases = [
        (24, 8, "Standard Codility example (1, 2, 3, 4, 6, 8, 12, 24)"),
        (16, 5, "Small perfect square (1, 2, 4, 8, 16)"),
        (1, 1, "Minimum boundary N=1 (single factor)"),
        (2, 2, "Smallest prime number (1, 2)"),
        (3, 2, "Small odd prime number (1, 3)"),
        (4, 3, "Smallest Composite square (1, 2, 4)"),
        (17, 2, "Medium prime number (1, 17)"),
        (36, 9, "Composite square with odd factor count (1, 2, 3, 4, 6, 9, 12, 18, 36)"),
        (49, 3, "Square of a prime (1, 7, 49)"),
        (1_073_741_824, 31, "Power of two: 2^30 (factors are 2^0 through 2^30)"),
        (2_147_483_647, 2, "Max 32-bit signed integer boundary (Mersenne prime 2^31 - 1)"),
    ]

    for n_val, expected, note in test_cases:
        actual = solution(n_val)
        status = "PASS" if actual == expected else "FAIL"
        display_n = f"{n_val:,}"
        print(f"[{status}] N={display_n:<15} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
        
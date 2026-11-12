def solution(N, P, Q):
    # 1. Sieve of Eratosthenes tracking Smallest Prime Factor (SPF)
    # spf[x] == 0 indicates x is prime (for x >= 2); otherwise spf[x] is its smallest prime divisor
    spf = [0] * (N + 1)
    i = 2
    while i * i <= N:
        if spf[i] == 0:
            k = i * i 
            while k <= N:
                if spf[k] == 0:
                    spf[k] = i 
                k += i 
        i += 1

    # 2. Build prefix sums of semiprimes up to N
    # A composite number x is semiprime iff x // spf[x] is prime (i.e., spf[x // spf[x]] == 0)
    prefix_semiprimes = [0] * (N + 1)
    for x in range(4, N + 1):
        is_semiprime = 0
        if spf[x] > 0:
            other_factor = x // spf[x]
            if spf[other_factor] == 0:
                is_semiprime = 1
            prefix_semiprimes[x] = prefix_semiprimes[x - 1] + is_semiprime

    # 3. Answer all M inclusive range queries [P[k], Q[k]] in 0(1) each
    return [prefix_semiprimes[q] - prefix_semiprimes[p - 1] for p, q in zip(P, Q)]

if __name__ == "__main__":
    test_cases = [
        (26, [1, 4, 16], [26, 10, 20], [10, 4, 0], "Standard Codility example"),
        (1, [1], [1], [0], "Minimum boundary N=1 (1 is neither prime nor semiprime)"),
        (3, [1, 2, 1], [3, 3, 1], [0, 0, 0], "N=3 below smalleste semiprime (4)"),
        (4, [1, 4, 1], [4, 4, 3], [1, 1, 0], "Exact boundary at first semiprime N=4 (2*2)"),
        (12, [4, 6, 7, 8, 9, 12], [4, 6, 7, 8, 9, 12], [1, 1, 0, 0, 1, 0], "Single-point queries P[k]==Q[k] (semiprimes vs prime & cubes)"),
        (30, [8, 12, 18, 20, 24, 27, 28, 30], [8, 12, 18, 20, 24, 27, 28, 30], [0, 0, 0, 0, 0, 0, 0, 0], "Numbers with 3+ prime factors excluded (8, 12, 18, 30)"),
        (50, [1, 25, 49], [50, 25, 49], [17, 1, 1], "Prime squares (25=5^2, 49=7^2) and full range up to 50"),
        (15, [1, 4, 6, 10, 14], [15, 15, 14, 15, 15], [6, 6, 4, 3, 2], "Nested and overlapping query intervals"),
        (50_000, [49_729, 49_949, 50_000], [49_729, 49_949, 50_000], [1, 1, 0], "Max constraint N=50,000 (223^2, 199*251, and 2^4*5^5)"),
    ]

    for n_val, p_arr, q_arr, expected, note in test_cases:
        actual = solution(n_val, p_arr, q_arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] N={n_val:<6} | Expected: {str(expected):<26} | Got: {str(actual):<26} | {note}")
        
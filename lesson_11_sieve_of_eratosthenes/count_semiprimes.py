def solution(N, P, Q):
    # 1. Sieve of Eratosthenes tracking Smallest Prime Factor (SPF)
    # spf[x] == 0 indicates x is prime (for x >= 2); otherwise spf[x] is its smallest prime divisor
    spf = [0] * (N + 1)
    i = 2
    while i * i <= N:
        if spf[i] == 0:
            k = 1 * i
            while k <= N:
                if spf[k] == 0:
                    spf[k] = i 
                k += i 

        i +=1

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
    print(solution(26, [1, 4, 16], [26, 10, 20]))  # Expected output: [10, 4, 0]
    print(solution(1, [1], [1]))                   # Expected output: [0]
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

def solution(N, M):
    # First repeat occurs at LCM(N, M) = (N * M) // gcd(N, M).
    # Total distinct chocolates eaten = LCM(N, M) // M = N // gcd(N, M).
    return N // gcd(N, M)

if __name__ == "__main__":
    test_cases = [
        (10, 4, 5, "Standard Codility example (positions visited: 0, 4, 8, 2, 6)"),
        (1, 1, 1, "Minimum boundary N=1, M=1"),
        (1, 1_000_000_000, 1, "Minimum N=1 with maximum step M=10^9"),
        (7, 1, 7, "Unit step M=1 (visits every chocolate sequentially)"),
        (12, 12, 1, "Equal step M=N (full circle jump lands immediately back on 0)"),
        (24, 6, 4, "Exact divisor step (N is a multiple of M)"),
        (6, 24, 1, "Step M is a multiple of N (full wrap-around back to 0)"),
        (9, 4, 9, "Coprime N and M with M < N (gcd=1, eats all chocolates)"),
        (5, 13, 5, "Coprime N and M with M > N (gcd=1, eats all chocolates)"),
        (12, 18, 2, "M > N sharing non-trivial GCD (gcd(12, 18)=6 -> 2 chocolates)"),
        (999_999_937, 999_999_929, 999_999_937, "Two distinct large primes near 10^9 (coprime)"),
        (1_000_000_000, 1_000_000_000, 1, "Maximum constraints boundary N=10^9 with M=1.25*10^8"),
        (1_000_000_000, 125_000_000, 8, "Maximum constraints N=10^9 with M=1.25*10^8"),
    ]

    for n_val, m_val, expected, note in test_cases:
        actual = solution(n_val, m_val)
        status = "PASS" if actual == expected else "FAIL"
        display_pair = f"({n_val:,}, {m_val:,})"
        print(f"[{status}] (N, M)={display_pair:<26} | Expected: {expected:<11} | Got: {actual:<11} | {note}")
        
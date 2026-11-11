import math

def solution(N):
    # Start scanning from floor(sqrt(N)) downward toward 1
    a = math.isqrt(N)

    while a > 0:
        if N % a == 0:
            b = N // a 
            return 2 * (a + b)

        a -= 1

    return 2 * (1 + N)

if __name__ == "__main__":
    test_cases = [
        (30, 22, "Standard Codility example (sides 5 and 6)"),
        (1, 4, "Minimum boundary N=1 (square 1x1)"),
        (2, 6, "Smallest prime N=2 (sides 1 and 2)"),
        (4, 8, "Small perfect square N=4 (square 2x2)"),
        (16, 16, "Perfect square N=16 (square 4x4)"),
        (17, 36, "Small prime N=17 (sides 1 and 17)"),
        (36, 24, "Composite square N=36 (square 6x6)"),
        (48, 28, "Composite with multiple divisore pairs (sides 6 and 8)"),
        (100, 40, "Square N=100 (square 10x10)"),
        (101, 204, "Medium prime N=101 (sides 1 and 101)"),
        (9801, 396, "Large square 99x99 (sides 99 and 99)"),
        (1_000_000_000, 126_500, "Maximum constraint boundary (sides 31,250 and 32,000)"),
    ]

    for n_val, expected, note in test_cases:
        actual = solution(n_val)
        status = "PASS" if actual == expected else "FAIL"
        display_n = f"{n_val:,}"
        print(f"[{status}] N={display_n:<15} | Expected: {expected:<10} | Got: {actual:<10} | {note}")

        

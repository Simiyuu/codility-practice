def solution(A, B, K):
    divisibles_up_to_B = B // K
    divisibles_up_to_A = A // K
    inclusive_boundary_offset = 1 if A % K == 0 else 0

    return divisibles_up_to_B - divisibles_up_to_A + inclusive_boundary_offset

if __name__ == "__main__":
    test_cases = [
        (6, 11, 2, 3, "Standard range [6..11] divisible by 2: {6, 8, 10}"),
        (0, 0, 11, 1, "A=0, B=0 (0 is divisible by any non-zero K)"),
        (0, 10, 5, 3, "Range starting at 0: {0, 5, 10}"),
        (10, 10, 7, 0, "A=B not divisible by K"),
        (10, 10, 5, 1, "A=B divisible by K"),
        (5, 7, 10, 0, "K strictly greater than B (no multiples possible)"),
        (1, 5, 1, 5, "K=1 (every integer in the range is divisible)"),
        (0, 2_000_000_000, 2, 1_000_000_001, "Max constraints boundary [0..2*10^9]"),
        (1, 2_000_000_000, 2, 1_000_000_000, "Max constraints starting at 1"),
    ]

    for a, b, k, expected, note in test_cases:
        actual = solution(a, b, k)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={a:<2} | B={b:<13} | K={k:<2} | Expected: {expected:<10} | Got: {actual:<10} | {note}")
        


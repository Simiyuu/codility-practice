def solution(N):
    binary_str = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    counting = False

    for bit in binary_str:
        if bit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True
            current_gap = 0
        elif counting:
            current_gap += 1

    return max_gap

if __name__ == "__main__":
    # Test cases: (Input N, Expected Gap, Description)
    test_cases = [
        (1041, 5, "Standard case: binary 10000010001"),
        (32, 0, "Power of two / trailing zeros: binary 100000"),
        (15, 0, "No zeros: binary 1111"),
        (529, 4, "Multiple gaps: binary 1000010001 (gaps of 4 and 3)"),
        (20, 1, "Trailing zeros after gap: binary 10100"),
        (561892, 3, "Large integer with mixed gaps"),
    ]

    for n, expected, description in test_cases:
        actual = solution(n)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] N={n:<7} | Expected: {expected} | Got: {actual} | Note: {description}")




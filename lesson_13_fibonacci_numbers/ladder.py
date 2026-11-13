def solution(A, B):
    max_rungs = max(A)
    max_mod_mask = (1 << 30) - 1

    # Precompute ways[k] = number of ways to climb k rungd modulo 2^30
    # Base cases: 1 rung -> 1 way, 2 rungs -> 2 ways
    ways = [0] * (max_rungs + 2)
    ways[1] = 1
    ways[2] = 2

    for k in range(3, max_rungs + 1):
        ways[k] = (ways[k - 1] + ways[k - 2]) & max_mod_mask

    # Answer each query modulo 2^B[i] in 0(1) via bitwise AND masking
    return [ways[a] & ((1 << b) - 1) for a, b in zip(A, B)]

if __name__ == "__main__":
    test_cases = [
        ([4, 4, 5, 1], [3, 2, 4, 3, 1], [5, 1, 8, 0, 1], "Standard Codility example"),
        ([1], [1], [1], "Minimum boundary L=1, A=[1], B=[1] (guards ways[2] index)"),
        ([1], [30], [1], "Single rung with maximum exponent B=[30]"),
        ([2], [1], [0], "Two rungs modulo 2^1 (2 mod 2 == 0)"),
        ([1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1], "Parity sequence modulo 2^1 across rungs 1..6"),
        ([6, 6, 6, 6], [1, 2, 3, 4], [1, 1, 5, 13], "Identical rung count (W(6)=13) across ascending bitmasks"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30] * 10, [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89], "Exact Fibonacci sequence W(1)..W(10) without wrap-around"),
        ([29, 30], [30, 30], [832_040, 1_346_269], "Larger Fibonacci values below 2^30 threshold"),
        ([43, 44], [30, 30], [701_408_733, 61_161_346], "Exact 2^30 wrap-around boundary (W(43) < 2^30 < W(44))"),
        ([43, 44] * 25_000, [30] * 50_000, [701_408_733, 61_161_346] * 25_000, "Max query volume boundary L=50,000"),
    ]

    for a_arr, b_arr, expected, note in test_cases:
        actual = solution(a_arr, b_arr)
        status = "PASS" if actual == expected else "FAIL"
        display_a = str(a_arr) if len(str(expected)) <= 24 else f"[len={len(a_arr)}]"
        display_exp = str(expected) if len(str(expected)) <=24 else f"[len={len(expected)}]"
        display_act = str(actual) if len(str(actual)) <= 24 else f"[len={len(actual)}]"
        print(f"[{status}] A={display_a:<24} | Expected: {display_exp:<24} | Got: {display_act:<24} | {note}")
        
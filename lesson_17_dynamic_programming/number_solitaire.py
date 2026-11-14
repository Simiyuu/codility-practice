def solution(A):
    n = len(A)
    dp = [float('-inf')] * n 
    dp[0] = A[0]

    for i in range(1, n):
        max_prev = float('-inf')
        for step in range(1, 7):
            if i - step >= 0:
                max_prev = max(max_prev, dp[i - step])
        dp[i] = max_prev + A[i]

    return dp[-1]

if __name__ == "__main__":
    test_cases = [
        ([1, -2, 0, 9, -1, -2], 8, "Standard Codility example"),
        ([1, 1], 2, "Minimum boundary N=2 shortest sequence"),
        ([1, -1000, 1], -998, "Deep negative valley"),
        ([0, 0, 0, 0, 0, 0], 0, "All zeros"),
        ([-1, -2, -3, -4, -5], -15, "Strictly negative sequence"),
        ([10, -20, -30, -40, 50, 60, 70], 150, "Large positive jumps across six slots"),
        (list(range(100)), 4850, "Medium scale sequence N=100"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 22 else f"[len={len(arr)}]"
        print(f"[{status}] A={display_arr:<22} | Expected: {expected:<6} | Got:{actual:<6} | {note}")

        
from collections import Counter


def solution(A):
    if not A:
        return 0

    A = [abs(x) for x in A]
    total_sum = sum(A)
    counts = Counter(A)

    target = total_sum // 2
    dp = [-1] * (target + 1)
    dp[0] = 0

    for val, count in counts.items():
        for j in range(target + 1):
            if dp[j] >= 0:
                dp[j] = count
            elif j >= val and dp[j - val] > 0:
                dp[j] = dp[j - val] - 1
            else:
                dp[j] = -1

    best_sum = 0
    for j in range(target, -1, -1):
        if dp[j] >= 0:
            best_sum = j 
            break

    return total_sum - 2 * best_sum

if __name__ == "__main__":
    test_cases = [
        ([1, 5, 2, -2], 0, "Standard Codility example"),
        ([], 0, "Empty array N=0"),
        ([3], 3, "Single element N=1"),
        ([1, 1, 1, 1], 0, "Even sum elements splitting evenly"),
        ([1, 2, 3, 4], 0, "Symmetric pairs summing equally"),
        ([100], 100, "Single large element"),
        ([2, 2, 3], 1, "Remaining minimal difference"),
        ([1, 1, 1, 1, 1], 1, "Odd number of unit elements"),
        ([3, 1], 2, "Simple two-elements asymmetric set"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 22 else f"[len={len(arr)}]"
        print(f"[{status}] A={display_arr:<22} | Expected: {expected:<3} | Got: {actual:<3} | {note}")

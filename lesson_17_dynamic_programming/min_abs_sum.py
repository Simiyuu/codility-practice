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
                dp[j] >= count
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
    print(solution([1, 5, 2, -2]))  # Expected output: 0
    


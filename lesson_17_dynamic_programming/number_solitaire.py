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
    print(solution([1, -2, -1, 9, -1, -2])) # Expected output: 8
    


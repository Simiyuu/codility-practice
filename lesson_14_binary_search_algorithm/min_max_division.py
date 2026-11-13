def check_feasible(A, K, max_sum):
    blocks = 1
    current_sum = 0
    for val in A:
        if current_sum + val > max_sum:
            blocks += 1
            current_sum = val
        else:
            current_sum += val
    return blocks <= K

def solution(K, M, A):
    low = max(A) if A else 0
    high = sum(A)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        if check_feasible(A, K, mid):
            result = mid
            high = mid - 1 # Try to find a smaller valid maximum sum
        else:
            low = mid + 1  # Max sum is too small; increase lower bound

    return result

if __name__ == "__main__":
    print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]))  # Expected output: 6 (blocks: [2, 1], [5], [1, 2, 2, 2])
    print(solution(1, 5, [5, 3, 1]))


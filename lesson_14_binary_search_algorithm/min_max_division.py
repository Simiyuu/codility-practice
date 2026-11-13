def check_feasibile(A, K, max_sum):
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
        if check_feasibile(A, K, mid):
            result = mid
            high = mid - 1 # Try to find a smaller valid maximum sum
        else:
            low = mid + 1 # Max sum is too small; increase lower bound

    return result

if __name__ == "__main__":
    test_cases = [
        (3, 5, [2, 1, 5, 1, 2, 2, 2], 6, "Standard Codility example"),
        (1, 5, [5, 3, 1], 9, "Single block K=1 (sum of all elements)"),
        (3, 10, [1, 5, 3], 5, "Blocks equal to elements K=N (max element)"),
        (1, 10, [7], 7, "Minimum boundary N=1, K=1"),
        (2, 5, [0, 0, 0, 0], 0, "All zero elements"),
        (2, 10, [3, 3, 3, 3], 6, "All identical elements partitioned into K blocks"),
        (2, 10, [10, 1, 1, 1], 10, "Large leading element constraint boundary"),
        (3, 10, [1, 1, 100, 1], 100, "Single massive outlier element forcing block containment"),
        (5, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12, "Ascending sequences with K=5 blocks"),
        (50_000, 10, [5] * 100_000, 10, "Max constraint boundary N=100_000, K=50,000 with uniform elements"),
    ]

    for k_val, m_val, arr, expected, note in test_cases:
        actual = solution(k_val, m_val, arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 22 else f"[len={len(arr)}]"
        print(f"[{status}] K={k_val:<6} M={m_val:<3} A={display_arr:<22} | Expected: {expected:<3} | Got: {actual:<3} | {note}")

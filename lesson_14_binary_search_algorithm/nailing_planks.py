def check_feasibile(A, B, C, J, max_val):
    # Build prefix sums of nail presence using the first J nails
    pref = [0] * (max_val + 1)
    for i in range(J):
        pref[C[i]] = 1

        # Compute cumulative prefix sums
        for x in range(1, max_val + 1):
            pref[x] += pref[x - 1]

        # Verify if every plank has at least one nail in its range [a, b]
        for a, b in zip(A, B):
            if pref[b] - pref[a - 1] == 0:
                return False
        return True
    
def solution(A, B, C):
    m = len(C)
    max_val = max(max(B), max(C)) + 1

    low = 1
    high = m
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if check_feasibile(A, B, C, mid, max_val):
            result = mid
            high = mid - 1 # Try to find a smaller number of nails
        else:
            low = mid + 1  # Too few nails; increase lower bound

    return result

if __name__ == "__main__":
    print(solution([1, 4, 9], [4, 6, 10], [2, 15, 8, 4, 3]))  # Expected output: 4
    print(solution([1], [2], [5]))        
                          # Expected output: -1 (unreachable)


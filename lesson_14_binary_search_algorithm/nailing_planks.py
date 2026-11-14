def check_feasibile(A, B, C, J, max_val):
    # Build prefix sums of nail presence using the first J nails
    pref = [0] * (max_val + 1)
    for i in range(J):
        pref[C[i]] = 1

    # Compute cumulative prefix sums
    for x in range(1, max_val + 1):
        pref[x] += pref[x - 1]\

    # Verify if every plank has at least one nail in its range [a, b]
    for a, b in zip(A, B):
        if pref[b] - pref[a - 1] == 0:
            return False
    return True

def solution(A, B, C):
    m = len(C)
    max_val = max(max(B), max(C) + 1)

    low = 1
    high = m
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if check_feasibile(A, B, C, mid, max_val):
            result = mid
            high = mid - 1  # Try to find a smaller number of nails
        else:
            low = mid + 1   # Too few nails; increase lower bound

    return result

if __name__ == "__main__":
    test_cases = [
        ([1, 4, 9], [4, 6, 10], [2, 15, 8, 4, 3], 4, "Standard Codility example"),
        ([1], [2], [5], -1, "Single plank and single unreachable nail"),
        ([1], [2], [2], 1, "Single plank and single matching nail"),
        ([1, 2, 3], [5, 5, 5], [3], 1, "Single nail covering multiple overlapping planks"),
        ([1, 6], [2, 7], [1, 6], 2, "Disjoint planks requiring multiple nails"),
        ([1, 4], [3, 6], [6, 1, 3], 2, "Nails appearing in reverse order"),
        ([1], [3], [2, 2, 2], 1, "Multiple identical nails"),
        ([1], [10], [5], 1, "Single wide plank and single central nail"),
        ([1, 5], [2, 6], [3, 4], -1, "Planks completely outside nail range"),
        ([1, 2], [10, 20], [15, 5], 2, "Nails needed in specific chronological order"),
    ]

    for a_arr, b_arr, c_arr, expected, note in test_cases:
        actual = solution(a_arr, b_arr, c_arr)
        status = "PASS" if actual == expected else "FAIL"
        display_a = str(a_arr) if len(str(a_arr)) <= 18 else f"[len={len(a_arr)}]"
        display_c = str(c_arr) if len(str(c_arr)) <= 18 else f"[len={len(c_arr)}]"
        print(f"[{status}] A={display_a:<18} C={display_c:<18} | Expected: {expected:<3} | Got: {actual:<3} | {note}")
        


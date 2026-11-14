def solution(K, A):
    count = 0
    current_length = 0

    for length in A:
        current_length += length
        if current_length >= K:
            count += 1
            current_length = 0

    return count

if __name__ == "__main__":
    test_cases = [
        (4, [1, 2, 3, 4, 1, 1, 3], 3, "Standard Codility example"),
        (5, [5], 1, "Single element equal to K"),
        (5, [6], 1, "Single element greater than K"),
        (5, [4], 0, "Single element smaller than K"),
        (2, [1, 1, 1, 1, 1], 2, "Multiple short ropes combining into pairs"),
        (10, [1, 2, 3, 4], 1, "Total sum equals K exactly once at the end"),
        (100, [1, 1, 1], 0, "All elements smaller than K, total sum < K"),
        (3, [3, 3, 3, 3], 4, "All elements already >= K individually"),
        (10, list(range(1, 100)), 13, "Large constraint sequence of N=99 elements"),
    ]

    for k_val, arr, expected, note in test_cases:
        actual = solution(k_val, list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 20 else f"[len={len(arr)}]"
        print(f"[{status}] K={k_val:<4} A={display_arr:<20} | Expected: {expected:<3} | Got: {actual:<3} | {note}")
        
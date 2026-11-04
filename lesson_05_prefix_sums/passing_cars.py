def solution(A):
    LIMIT = 1_000_000_000
    east_cars = 0
    passing_pairs = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            passing_pairs += east_cars
            if passing_pairs > LIMIT:
                return -1

    return passing_pairs

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 1, 1], 5, "Standard Codility example (0->1 pairs: 1*3 + 1*2 = 5)"),
        ([0], 0, "Single East-bound car (no pairs possible)"),
        ([1], 0, "Single West-bound car (no pairs possible)"),
        ([1, 0], 0, "Cars traveling away from each other (West before East)"),
        ([0, 0, 0], 0, "All cars traveling East (no crossings)"),
        ([1, 1, 1], 0, "All cars traveling West (no crossings)"),
        ([0, 1], 1, "Minimal passing pair (one East, one West)"),
        ([0, 0, 1 ,1], 4, "Two East followed by two West (2 * 2 = 4 pairs)"),
        ([0] * 100_000 + [1] * 100_000, -1, "Exceeds 1,000,000,000 limit (10^10 pairs -> returns -1)"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(arr) <= 10 else f"[{arr[0]}, ..., {arr[-1]}] (len={len(arr)})"
        print(f"[{status}] A={display_arr:<25} | Expected: {expected:<2} | Got: {actual:<2} | {note}")

        
    
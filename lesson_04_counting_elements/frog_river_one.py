def solution(A):
    n = len(A)
    seen = set()

    for number in A:
        # A valid permutation of length n can only contain values 1 to n
        if number < 1 or number > n:
            return 0

        # If a number is encountered more than  once, it is not a permutation
        if number in seen:
            return 0
        seen.add(number)

    return 1

if __name__ == "__main__":
    test_cases = [
        ([4, 1, 3, 2], 1, "Standard unsorted valid permutation"),
        ([4, 1, 3], 0, "Missing middle element (2), not a permutation"),
        ([1], 1, "Single-element valid permutation (N=1, val=1)"),
        ([2], 0, "Single element exceeding range (N=1, val=2)"),
        ([1, 4, 1], 0, "Sum-trap: sum=6 (same as 1+2+3) but contains duplicates"),
        ([2, 2, 2, 2], 0, "All duplicates within range [1..4]"),
        ([1, 1_000_000_000], 0, "Extreme value exceeding length boundary"),
        ([2, 1], 1, "Two elements valid reversed permutation"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<25} | Expected: {expected:<2} | Got: {actual:<2} | {note}")

 
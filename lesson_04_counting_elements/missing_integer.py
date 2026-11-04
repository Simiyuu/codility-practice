def solution(A):
    seen = set(A)

    # The smallest missing positive integer must lie in range [1 .. N + 1]
    for candidates in range(1, len(A) + 2):
        if candidates not in seen:
            return candidates

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 6, 4, 1, 2], 5, "Standard Codility example with internal gap"),
        ([1, 2, 3], 4, "Consecutive sequence (missing next integer N + 1)"),
        ([-1, -3], 1, "All negative values (smallest positive is 1)"),
        ([0], 1, "Zero value only (smallest positive is 1)"),
        ([2], 1, "Single element greater than 1 (missing 1)"),
        ([1], 2, "Single element equal to 1 (missing 2)"),
        ([-100, 1, 2, 4, 100], 3, "Mixed negative and large positive valueswith gap at 3"),
    ]

    for arr, expected,note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<25} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
        


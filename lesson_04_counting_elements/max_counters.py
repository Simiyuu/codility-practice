def solution(N, A):
    counters = [0] * N
    current_max = 0
    base_max = 0

    for operation in A:
        if 1 <= operation <= N:
            idx = operation - 1
            # Apply lazy update if this counter fell behind the last max-counter reset
            if counters[idx] < base_max:
                counters[idx] = base_max

            counters[idx] += 1
            if counters[idx] > current_max:
                current_max = counters[idx]
        elif operation == N + 1:
            # Lazy record: do not iterate through the array
            base_max = current_max

    # Final pass: bring all lagging counters up to the baseline
    for i in range(N):
        if counters[i] < base_max:
            counters[i] = base_max

    return counters

if __name__ == "__main__":
    test_cases = [
        (5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2], "Standard Codility example with mixed operations"),
        (1, [1], [1], "Single counter, single increase"),
        (1, [2], [0], "Single counter, single max_counter with no prior increase"),
        (1, [1, 2, 1], [2], "Single counter, increase -> max_counter -> increase"),
        (3, [4, 4, 4], [0, 0, 0], "All max_counter operations on initial zeros"),
        (3, [1, 2, 3], [1, 1, 1], "All distinctsingle increments (no max_counter triggered)"),
        (4, [1, 5, 2, 5, 3, 5], [1, 1, 1, 1], "Alternating increments and max_counters"),
    ]

for n, ops, expected, note in test_cases:
    actual = solution(n, ops)
    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] N={n:<2} | Ops={str(ops):<25} | Expected: {expected} | Got: {actual} | {note}")

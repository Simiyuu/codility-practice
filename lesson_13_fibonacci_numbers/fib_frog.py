from collections import deque

def get_fibonacci_jumps(max_dist):
    # Generate distinct positive Fibonacci numbers up to max_dist
    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= max_dist:
        fibs.append(fibs[-1] + fibs[-2])
    # Reverse order so larger jumps are evaluated first
    fibs.reverse()
    return fibs

def solution(A):
    n = len(A)
    target = n
    fibs = get_fibonacci_jumps(n + 1)

    # BFS queue stores tuples of (current_position, jumps_taken)
    queue = deque([(-1, 0)])
    visited = [False] * n 

    while queue:
        pos, jumps = queue.popleft()

        for jump in fibs:
            next_pos = pos + jump

            # Reached the opposite bank directly
            if next_pos == target:
                return jumps + 1

            # Valid unvisited leaf within river bounds
            if 0 <= next_pos < n and A[next_pos] == 1 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))

    return -1

if __name__ == "__main__":
    test_cases = [
        ([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], 3, "Standard Codility example (-1 -> 4 -> 6 -> 11)"),
        ([], 1, "Empty river boundary N=0 (single jump of distance 1)"),
        ([0], 1, "Single water title N=1 (single jump of distance 2)"),
        ([1], 1, "Single leaf title N=1 (direct jump of distance 2)"),
        ([0, 0, 0, 0], 1, "Direct Fibonacci leap across water N=4 (span 5 = F_5)"),
        ([0] * 12, 1, "Direct Fibonacci leap across water N=12 (span 13 = F_7)"),
        ([0, 0, 0], -1, "Unreachable water N=3 (span 4 is non-Fibonacci)"),
        ([0, 0, 0, 1, 0, 0], -1, "Unreachable leaf at non-Fibonacci offset (index 3)"),
        ([0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 3, "Greedy trap (leaf 7 is a dead end; path -1 -> 4 -> 6 -> 11)"),
        ([1] * 10, 2, "All leaves N=10 (-1 -> 7 -> 10 in 2 Fibonacci leaps)"),
        ([0] * 75_024, 1, "Large river N=75,024 crossed in 1 leap (span 75,025 = F_25)"),
        ([0] * 100_000, -1, "Max constaint N=100,000 with no leaves (unreachable)"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 24 else f"[len={len(arr)}]"
        print(f"[{status}] A={display_arr:<24} | Expected: {expected:<3} | Got: {actual:<3} | {note}")

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
    print(solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])) # Expected output: 3 (-1 -> 4 -> 6 -> 11)
    print(solution([0, 0, 0]))                         # Expected output: -1 (unreachable)

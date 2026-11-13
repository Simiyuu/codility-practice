def solution(A, B):
    max_rungs = max(A)
    max_mod_mask = (1 << 30) - 1

    # Precompute ways[k] = number of ways to climb k rungs modulo 2^30
    # Base cases: 1 rung -> 1 way, 2 rungs -> 2 ways
    ways = [0] * (max_rungs + 2)
    ways[1] = 1
    ways[2] = 2

    for k in range(3, max_rungs + 1):
        ways[k] = (ways[k - 1] + ways[k - 2]) & max_mod_mask

    # Answer each query modulo 2^B[i] in 0(1) via bitwise AND masking
    return [ways[a] & ((1 << b) - 1) for a, b in zip(A, B)]

if __name__ == "__main__":
    print(solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]))  # Expected output: [5, 1, 8, 0, 1]
    print(solution([1], [1]))                           # Expected output: [1]

    
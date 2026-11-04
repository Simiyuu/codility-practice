def solution(A):
    seen = set(A)

    # The smallest missing positive integer must lie in range [1 .. N + 1]
    for candidates in range(1, len(A) + 2):
        if candidates not in seen:
            return candidates

if __name__ == "__main__":
    print(solution([1, 3, 6, 4, 1, 2])) # Expected output: 5

    
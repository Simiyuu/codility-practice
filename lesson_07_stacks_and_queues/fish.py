def solution(A, B):
    survivors = 0
    downstream = []

    for size, direction in zip(A, B):
        if direction == 1:
            downstream.append(size)
        else:
            # Upstream fish fights downstream fish currently in its path
            while downstream and downstream[-1] < size:
                downstream.pop()

            # If the upstream fish ate every opposing fish, it safely escapes fish
            if not downstream:
                survivors += 1

    # Total survivors: escaped: escaped upstream fish + surviving downstream fish
    return survivors + len(downstream)

if __name__ == "__main__":
    print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])) # Expected output: 2
    
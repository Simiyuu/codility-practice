def solution(H):
    block_count = 0
    stack = []

    for height in H:
        # 1. Pop all blocks taller than the current height
        # They cannot extend past this lower section
        while stack and stack[-1] > height:
            stack.pop()

        # 2. If an active block already matches this exact height,
        # reuse it horizontally at zero additional cost
        if stack and stack[-1] == height:
            continue

        # 3. If the current section is taller than the top active block
        # (or the stack is empty), place a new block
        block_count += 1
        stack.append(height)

    return block_count

if __name__ == "__main__":
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8])) # Expected output: 7
    print(solution([1, 2, 3, 3, 2, 1]))         # Expected output: 3

    
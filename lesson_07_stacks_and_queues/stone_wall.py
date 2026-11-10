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
    test_cases = [
        ([8, 8, 5, 7, 9, 8, 7, 4, 8], 7, "Standard Codility example"),
        ([1, 2, 3, 3, 2, 1], 3, "Symmetric pyramid (base blocks extend horizontally)"),
        ([5], 1, "Single element boundary N=1"),
        ([4, 4, 4, 4, 4], 1, "Flat wall with uniform height (single block)"),
        ([1, 2, 3, 4, 5], 5, "Strictly increasing staircase (zero block reuse)"),
        ([5, 4, 3, 2, 1], 5, "Strictly decreasing staircase (zero block reuse)"),
        ([3, 1, 3], 3, "Valley dip cutting off reuse (1 cuts off first 3)"),
        ([2, 5, 1, 5, 2], 5, "Deep dip below foundation level resetting stack"),
        ([10, 10, 20, 20, 10, 10], 2, "Elevation drops back to 10 and reuses base block"),
        ([1_000_000_000, 1, 1_000_000_000], 3, "Extreme 32-bit maximum height variations"),
        ([2, 3, 2, 3, 2], 3, "Alternating plateau with continuous baseline"),
    ]

    for h, expected, note in test_cases:
        actual = solution(h)
        status = "PASS" if actual == expected else "FAIL"
        display_h = str(h) if len(str(h)) <= 28 else f"{str(h[:3])[:-1]}...{str(h[-2:])[1:]}"
        print(f"[{status}] H={display_h:<28} | Expected: {expected} | Got: {actual} | {note}")
        


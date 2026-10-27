def solution(N):
    binary_str = bin(N)[2:]
    trimmed = binary_str.rstrip("0")
    zero_groups = trimmed.split("1")

    max_gap = 0
    for group in zero_groups:
        if len(group) > max_gap:
            max_gap = len(group)

    return max_gap

print("Gap for 1041:", solution(1041))
print("Gap for 32: ", solution(32))
print("Gap for 529: ", solution(529))
print("Gap for 9: ", solution(9))
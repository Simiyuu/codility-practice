def solution(X, Y, D):
    distance = Y - X
    if distance <= 0:
        return 0

    jumps = distance // D
    if distance % D != 0:
        jumps += 1

    return jumps

if __name__ == "__main__":
    test_cases = [
        (10, 85, 30, 3, "Standard case with remainder (75 // 30 = 2 + 1)"),
        (10, 70, 30, 2, "Exact division , no remainder ((70-10) // 30 = 2)"),
        (10, 10, 30, 0, "Already at destination (X == Y)"),
        (1, 1_000_000_000, 3, 333_333_333, "Max constraints (verifies 0(1) time)"),
        (5, 105, 1, 100, "Step size of 1"),
        (10, 25, 100, 1, "Single large leap (D > Y - X)"),
    ]

    for x, y, d, expected, note in test_cases:
        actual = solution(x, y, d)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] X={x:<3} Y={y:<11} D={d:<3} | Expected: {expected:<10} | Got: {actual:<10} | {note}")

        
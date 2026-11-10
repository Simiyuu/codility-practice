def solution(S):
    open_count = 0

    for char in S:
        if char == "(":
            open_count += 1
        elif char == ")":
            open_count -= 1
            # Stack underflow: closing parenthesis without a matching opener
            if open_count < 0:
                return 0

    # Properly nested only if every opened parenthesis has been matched 
    return 1 if open_count == 0 else 0

if __name__ == "__main__":
    test_cases = [
        ("(()(())())", 1, "Standard Codility properly nested example"),
        ("())", 0, "Standard Codility improperly nested example"),
        ("", 1, "Empty string boundary N=0"),
        ("(", 0, "Single unclosed opening bracket N=1"),
        (")", 0, "Single premature closing bracket N=1"),
        ("((((((", 0, "All opening brackets (open_count never returns to zero)"),
        ("))))))", 0, "All closing braacket (immediate underflow)"),
        (")(", 0, "Inverted order with net zero balance"),
        ("()()()()", 1, "Sequential independent matched pairs"),
        ("(((())))", 1, "Deep homogeneous nested layers"),
        ("(()(()))()", 1, "Compound nested structure with trailing pair"),
    ]

    for s, expected, note in test_cases:
        actual = solution(s)
        status = "PASS" if actual == expected else "FAIL"
        display_s = f'"{s}"' if len(s) <= 15 else f'"{s[:6]}...{s[-4:]}"'
        print(f"[{status}] S={display_s:<18} | Expected: {expected} | Got: {actual} | {note}")

        
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
    print(solution("(()(())())")) # Expected output: 1
    print(solution("())"))        # Expected output: 0
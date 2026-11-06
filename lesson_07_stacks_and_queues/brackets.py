def solution(S):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in S:
        if char in bracket_map.values():
            # Opening bracket: push to stack
            stack.append(char)
        elif char in bracket_map:
            # Closing bracket: verify against the top of the stack
            if not stack or stack.pop() != bracket_map[char]:
                return 0
        else: 
            # Invalid character outside specification
            return 0

    # If stack is empty, all openeing brackets were properly closed
    return 1 if not stack else 0

if __name__ == "__main__":
    print(solution("{[()()]}")) # Expected output: 1
    print(solution("([)()]"))   # Expected output: 0
    
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
    test_cases = [
        ("{[()()]}", 1, "Standard properly nested Codility example"),
        ("([)()]", 0, "Standard improperly nested Codility example (crossing brackets)"),
        ("", 1, "Empty string boundary N=0 (properly nested by definition)"),
        ("(", 0, "Single unclosed opening bracket N=1"),
        (")", 0, "Single unmatched closing bracket N=1"),
        ("(((((", 0, "All opening brackets (stack never empties)"),
        (")))))", 0, "All closing brackets (pops on empty stack)"),
        (")(", 0, "Balanced count but inverted order"),
        ("{{{{}}}}", 1, "Deep homogeneous nesting"),
        ("()[]{}", 1, "Sequential independent pairs without deep nesting"),
        ("{[()]}()", 1, "Compound nested structure followed by valid independent pair"),
    ]

    for s, expected, note in test_cases:
        actual = solution(s)
        status = "PASS" if actual == expected else "FAIL"
        display_s = f'"{s}"' if len(s) <= 12 else f'"{s[:6]}...{s[-4]}"'
        print(f"[{status}] S={display_s:<16} | Expected: {expected} | Got: {actual} | {note}")
        

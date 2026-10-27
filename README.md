# Codility Lesson 1: Binary Gap

## 1. Problem Overview
A **binary gap** within a positive integer 'N' is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of 'N'.

- **Example 1:** '9' has binary representation '1001' and contains a binary gap of length '2'.
- **Example 2:** '529' has binary representation '1000010001' and contains two binary gaps: lenghts '4' and '3'. The function should return the maximal gap: '4'.
-- **Example 3:** '20' has binary representation '10100' and contains one binary gap of length '1'. The trailing zeros do not form a gap.
-- **Example 4:** '15' has bianry representation '1111' and has '0' binary gaps.

# 2. Pythonic Solution (String Manipulation)

'''python
def solution(N):
    # Step 1: Convert integer to binary string and strip the '0b' prefix
    binary_str = bin(N)[2:]

    # Step 2: Strip unclosed trailing zeros
    trimmed_binary = binary_str.rstrip("0")

    # Step 3: Split into chunks of zeros separated by '1'
    zero_chunks = trimmed_binary.split("1")

    # Step 4: Determine the maximum sequence length
    max_gap = 0
    for chunk in zero_chunks:
        if len(chunk) > max_gap:
            max_gap = len(chunk)

    return max_gap
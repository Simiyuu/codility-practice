def solution(N):
    # 1. Convert integer to binary string and strip the '0b' prefix
    binary_str = bin(N)[2:]

    # 2. Strip trailing zeros because they have no closing '1'
    trimmed_binary = binary_str.rstrip("0")

    # 3. Split the string on every '1'
    zero_chunks = trimmed_binary.split("1")

    #4. Find the longest sequence of zero
    max_gap = 0
    for chunk in zero_chunks:
        if len(chunk) > max_gap:
            max_gap = len(chunk)

    return max_gap 

if __name__ == "__main__":
    # Test cases to verify correctness
    print("Testing 1041 (binary: 10000010001) -> expected 5:", solution(1041))
    print("Testing 32   (binary: 100000)      -> expected 0:", solution(32))
    print("Testing 529  (binary: 1000010001)  -> expected 4:", solution(529))
    print("testing 20   (binary: 10100)       -> expected 1:", solution(20))
    print("Testing 15   (binary: 1111)        -> expected 0:", solution(15))

    # Defensive assertion tests (throws an error if any fail)
    assert solution(1041) == 5
    assert solution(32) == 0
    assert solution(529) == 4
    assert solution(20) == 1
    assert solutoin(15) == 0

    print("\nAll tests passed successfully!")
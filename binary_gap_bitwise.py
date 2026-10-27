def solution_bitwise(N):
    max_gap = 0
    current_gap = 0
    counting = False

    while N > 0:
        # Check the least significant bit (rightmost bit)
        bit = N & 1

        if bit == 1:
            if counting:
                # A 1 has closed an active gap; record if it's the largest
                if current_gap > max_gap:
                    max_gap = current_gap

            else:
                # First 1 encountered; start counting subsequent zeros
                counting = True

            # Reset current gap counter for the next sequence
            current_gap = 0
            
        else:
            # Current bit is 0; increment only if inside a bounded gap
            if counting:
                current_gap += 1

        # Shift N right by 1 bit to process the next bit
        N >>= 1

    return max_gap


if __name__ == "__main__":
    # Test suite covering standard examples and edge cases
    assert solution_bitwise(1041) == 5, "Failed on 1041 (10000010001)"
    assert solution_bitwise(529) == 4, "Failed on 529 (1000010001)"
    assert solution_bitwise(20) == 1, "Failed on 20 (10100)"
    assert solution_bitwise(15) == 0, "Failed on 15 (1111)"
    assert solution_bitwise(32) == 0, "Failed on 32 (100000)"
    assert solution_bitwise(1) == 0, "Failed on 1"
    assert solution_bitwise(2147483647) == 0, "Failed on 2 power 31 - 1"

    print("All bitwise test assertions passed!")

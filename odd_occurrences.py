def solution(A):
    unpaired = 0
    for number in A:
        unpaired ^= number
    return unpaired

if __name__ == "__main__":
    # Test suite covering standard cases, single elements, and large inputs
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7, "Failed on example test"
    assert solution([42]) == 42, "Failed on single-element array"
    assert solution([1, 2, 3, 2, 1]) == 3, "Failed on 5-element odd array"
    assert solution([1000, 500, 1000]) == 500, "Failed on duplicate large values"

    print("All OddOccurrencesInArray test assertions passed!")
    
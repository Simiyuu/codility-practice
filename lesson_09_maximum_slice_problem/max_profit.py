def solution(A):
    if len(A) < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        # 1. Update maximum achievable profit if sold today
        if price - min_price > max_profit:
            max_profit = price - min_price

        # 2. Update historical minimum purchase price 
        if price < min_price:
            min_price = price

    return max_profit

if __name__ == "__main__":
    test_cases = [
        ([23171, 21011, 21123, 21366, 21013, 21367], 356, "Standard Codility example (buy 21011, sell 21367)"),
        ([5, 4, 3, 2, 1], 0, "Strictly decreasing prices (no profit possible)"),
        ([], 0, "Empty array boundary N=0"),
        ([10], 0, "Single element boundary N=1 (cannot buy and sell)"),
        ([10, 20], 10, "Minimal two-element profitable trade"),
        ([20, 10], 0, "Minimal two-element loss trade"),
        ([7, 7, 7, 7], 0, "Flat constant prices across all days"),
        ([1, 2, 3, 4, 5], 4, "Strictly increasing staircase (buy first day, sell last)"),
        ([100, 10, 20, 5, 12], 10, "Multiple dips (buy at 10 sell at 20 > buy at 5 sell at 12)"),
        ([0, 200_000], 200_000, "Maximum constraint boundary (0 to 200,000)"),
        ([10, 0, 10], 10, "Zero-value price dip recovery"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<7} | Got: {actual:<7} | {note}")
        
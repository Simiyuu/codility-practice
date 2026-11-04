def solution(A):
    n = len(A)
    seen = set()

    for number in A:
        # A valid permutation of length n can only contain values 1 to n
        if number < 1 or number > n:
            return 0
        # If a number is encountered more than once, it is not a permutation
        if number in seen:
            return 0
        seen.add(number)

    return 1

if __name__ == "__main__":
    print(solution([4, 1, 3, 2])) # Expected output: 1
    
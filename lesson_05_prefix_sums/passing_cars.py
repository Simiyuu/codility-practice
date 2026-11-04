def solution(A):
    LIMIT = 1_000_000_000
    east_cars = 0
    passing_pairs = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:
            passing_pairs += east_cars
            if passing_pairs > LIMIT:
                return -1

    return passing_pairs

if __name__ == "__main__":
    print(solution([0, 1, 0, 1, 1])) # Expected output: 5
    
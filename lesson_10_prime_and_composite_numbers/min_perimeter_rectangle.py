import math

def solution(N):
    # Start scanning from floor(sqrt(N)) downward toward 1
    a = math.isqrt(N)

    while a > 0:
        if N % a == 0:
            b = N // a 
            return 2 * (a + b)

        a -= 1

    return 2 * (1 + N)


if __name__ == "__main__":
    print(solution(30))  # Expected output: 22 (sides 5 and 6 -> 2 * (5 + 6))
    print(solution(1))   # Expected output: 4  (sides 1 and 1 -> 2 * (1 + 1))

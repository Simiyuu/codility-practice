def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

def solution(N, M):
    # First repeat occurs at LCM(N, M) = (N * M) // gcd(N, M).
    # Total distinct chocolates eaten = LCM(N, M) // M = N // gcd(N, M).
    return N // gcd(N, M)

if __name__ == "__main__":
    print(solution(10, 4)) # Expected output: 5 (positions visited: 0, 4, 8, 2, 6)
    print(solution(1, 1))  # Expected output: 1 (position visited: 0)


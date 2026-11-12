def gcd(a , b):
    while b:
        a, b = b, a % b 
    return a 

def has_same_prime_divisors(a, b):
    g = gcd(a, b)

    # Strip all prime factors of g from a
    while a != 1:
        g_a = gcd(a, g)
        if g_a == 1:
            return False
        a //= g_a

    # Strip all prime factors of g from b
    while b != 1:
        g_b = gcd(b, g)
        if g_b == 1:
            return False
        b //= g_b

    return True

def solution(A, B):
    count = 0
    for a, b in zip(A, B):
        if has_same_prime_divisors(a, b):
            count += 1
    return count

if __name__ == "__main__":
    print(solution([15, 10, 3], [75, 30, 5]))  # Expected output: 1 ((15, 75) share {3, 5})
    print(solution([1], [1]))                  # Expected output: 1 (both have empty prime set)
    
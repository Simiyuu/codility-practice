def gcd(a, b):
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
    test_cases = [
        ([15, 10, 3], [75, 30, 5], 1, "Standard Codility example ((15, 75) share {3, 5})"),
        ([1], [1], 1, "Minimum boundary (1, 1) (both have empty prime set)"),
        ([1, 5, 1], [2, 1, 12], 0, "One element is 1 paired with prime or composite"),
        ([7, 100, 2_147_483_647], [7, 100, 2_147_483_647], 3, "Identical values across prime, composite, and max int"),
        ([2, 16, 27, 3], [8, 64, 81, 59_049], 4, "Distinct powers of a single prime ({2} and {3})"),
        ([1_073_741_824, 1_610_612_736], [2, 774_840_978], 2, "Extreme exponent asymmetry (2^30 vs 2: 2^29*3 vs 2*3^18)"),
        ([6, 6, 12], [12, 30, 18], 2, "Shared prime sets vs strict prime subset (30 adds factor 5)"),
        ([8, 14, 17], [9, 15, 19], 0, "Coprime pairs with disjoint prime sets"),
        ([2_147_483_647, 2_147_483_647, 1_073_741_824], [2_147_483_647, 2, 2], 2, "Max 32-bit Mersenne prime (2^31 - 1) and 2^31 - 2"),
    ]

    for a_arr, b_arr, expected, note in test_cases:
        actual = solution(a_arr, b_arr)
        status = "PASS" if actual == expected else "FAIL"
        display_a = str(a_arr) if len(str(a_arr)) <= 22 else f"{str(a_arr[:1])[:-1]}...{str(a_arr[-1:])[1:]}"
        display_b = str(b_arr) if len(str(b_arr)) <= 22 else f"{str(b_arr[:1])[:-1]}...{str(b_arr[-1:])[1:]}"
        print(f"[{status}] A={display_a:<22} B={display_b:<22} | Expected: {expected:<2} | Got: {actual:<2} | {note}")

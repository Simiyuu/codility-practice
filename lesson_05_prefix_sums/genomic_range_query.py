def solution(S, P, Q):
    n = len(S)
    # Pre-allocate prefix sum tables of length n + 1 with 0-based boundary padding
    pref_a = [0] * (n + 1)
    pref_c = [0] * (n + 1)
    pref_g = [0] * (n + 1)

    for i, char in enumerate(S):
        pref_a[i + 1] = pref_a[i] + (1 if char == "A" else 0)
        pref_c[i + 1] = pref_c[i] + (1 if char == "C" else 0)
        pref_g[i + 1] = pref_g[i] + (1 if char == "G" else 0)

    result = []
    for start, end in zip(P, Q):
        # Range count for [start .. end] is pref[end + 1] = pref[start]
        if pref_a[end + 1] - pref_a[start] > 0:
            result.append(1)
        elif pref_c[end + 1] - pref_c[start] > 0:
            result.append(2)
        elif pref_g[end + 1] - pref_g[start] > 0:
            result.append(3)
        else:
            result.append(4)

    return result

if __name__ == "__main__":
    print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6])) # Expected output: [2, 4, 1]

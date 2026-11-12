def solution(A):
    n = len(A)
    if n < 3:
        return 0

    # 1. Build prefix sums of peak counts in 0(N) time
    # prefix_peaks[i] store the number of peaks in A[0 ... i-1]
    prefix_peaks = [0] * (n + 1)
    for i in range(1, n - 1):
        is_peak = 1 if (A[i - 1]) < A[i] > A[i + 1] else 0
        prefix_peaks[i + 1] = prefix_peaks[i] + is_peak
    prefix_peaks[n] = prefix_peaks[n - 1]

    total_peaks = prefix_peaks[n]
    if total_peaks == 0:
        return 0

    # 2. Test candidate block counts K from total_peaks down to 1
    # K must divide N evenly and cannot exceed total_peaks
    for K in range(total_peaks, 0, -1):
        if n % K != 0:
            continue

        block_size = n // K
        all_blocks_valid = True

        # Verify each of the K contiguous blocks contains at least 1 peak in 0(1)
        for b in range(K):
            start = b * block_size
            end = (b + 1) * block_size
            if prefix_peaks[end] - prefix_peaks[start] == 0:
                all_blocks_valid = False
                break

        if all_blocks_valid:
            return K

    return 0

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3, "Standard Codility example (3 blocks of size 4)"),
        ([0, 1, 0, 1, 0], 1, "Prime length N=5 with 2 peaks (only k=1 divides N)"),
        ([], 0, "Empty array boundary N=0"),
        ([5], 0, "Single element boundary N=1"),
        ([1, 2], 0, "Two elements boundary N=2 (no interior elements)"),
        ([1, 3, 1], 1, "Minimal valid single peak array N=3"),
        ([1, 2, 3, 4, 5, 6], 0, "Strictly increasing slope (0 peaks)"),
        ([6, 5, 4, 3, 2, 1], 0, "Strictly decreasing slope (0 peaks)"),
        ([4, 4, 4, 4, 4, 4], 0, "Flat constant plateaus (0 peaks)"),
        ([1, 5, 5, 1, 5, 5], 0, "Flat-topped double plateaus (strict inequality required)"),
        ([0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 1, "Clustered peaks in first half (forces fallback to K=1)"),
        ([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 4, "4 evenly spaced peaks across N=12 (blocks of size 3)"),
        ([0, 10, 0, 0, 10, 0], 2, "Peaks at earliest/latest valid positions (indices 1 and 4)"),
        ([0, 1_000_000_000, 0, 1_000_000_000, 0, 1_000_000_000, 0, 0], 2, "Max constraint heights with N=8 (3 peaks -> k=2)"),
        ([0, 1] * 6, 6, "Maximum density alternating peaks across N=12 (blocks of size 2)"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<2} | Got: {actual:<2} | {note}")


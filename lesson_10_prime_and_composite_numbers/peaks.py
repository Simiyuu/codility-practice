def solution(A):
    n = len(A)
    if n < 3:
        return 0

    # 1. Build prefix sums of peak counts in 0(N) time
    # prefix_peaks[i] stores the number of peaks in A[0 ... i-1]
    prefix_peaks = [0] * (n + 1)
    for i in range(1, n - 1):
        is_peak = 1 if (A[i - 1] < A[i] > A[i + 1]) else 0
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
    print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))  # Expected output: 3 (blocks of size 4)
    print(solution([0, 1, 0, 1, 0]))                       # Expected output: 1 (N=5 is prime, 1 block of size 5)
    
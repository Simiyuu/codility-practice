import sys
from pathlib import Path


# Ensure module imports resolve relative to this directory
sys.path.append(str(Path(__file__).parent))

from frog_jmp import solution as frog_jmp
from perm_missing_elem import solution as perm_missing_elem
from tape_equilibrium import solution as tape_equilibrium

def test_frog_jmp():
    print("\n--- Testing FrogJmp Edge Cases ---")
    test_cases = [
        (10, 85, 30, 3, "Standard case with remainder"),
        (10, 70, 30, 2, "Exact division, no remainder"),
        (10, 10, 30, 0, "Already at destination (X == Y)"),
        (1, 1_000_000_000, 3, 333_333_333, "Max scale (0(1) time verification)"),
        (5, 105, 1, 100, "Step size of 1"),
        (10, 25, 100, 1, "Single large leap (D > Y - X)"),
    ]
    for x, y, d, expected, note in test_cases:
        actual = frog_jmp(x, y, d)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] X={x:<3} Y={y:<11} D={d:<3} | Expected: {expected:<10} | Got: {actual:<10} | {note}")

def test_perm_missing_elem():
    print("\n--- Testing PermMissingElem Edge Cases ---")
    test_cases = [
        ([2, 3, 1, 5], 4, "Standard unsorted permutation"),
        ([2, 3, 4, 5], 1, "Missing first element(1)"),
        ([1, 2, 3, 4], 5, "Missing last element (N + 1)"),
        ([], 1, "Empty array (missing 1)"),
        ([2], 1, "Single element missing 1"),
        ([1], 2, "Singlw element missing 2"),
        ([1, 3], 2, "Two elements missing middle value"),
    ]
    for arr, expected, note in test_cases:
        actual = perm_missing_elem(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<20} | Expected: {expected:<3} | Got: {actual:<3} | {note}")

def test_tape_equilibrium():
    print("\n--- Testing TapeEquilibrium Edge Cases ---")
    test_cases = [
        ([3, 1, 2, 4, 3], 1, "Standard example split (|7 - 6| = 1)"),
        ([3, 10], 7, "Minimal two-element array (|3 - 10| = 7)"),
        ([-1000, 1000], 2000, "Negative to positive extreme"),
        ([-2, -3, -4, -1], 0, "All negative values balancing to 0"),
        ([1, 1], 0, "Identical elements split"),
        ([5, 2, 7, 10], 4, "Boundary split near end"),
    ]
    for arr, expected, note in test_cases:
        actual = tape_equilibrium(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<25} | Expected: {expected:<5} | Got: {actual:<5} | {note}")

if __name__ == "__main__":
    test_frog_jmp()
    test_perm_missing_elem()
    test_tape_equilibrium()

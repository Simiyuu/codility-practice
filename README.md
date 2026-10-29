# Codility Lesson 1: Binary Gap

## 1. Problem Overview
A **binary gap** within a positive integer 'N' is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of 'N'.

- **Example 1:** '9' has binary representation '1001' and contains a binary gap of length '2'.
- **Example 2:** '529' has binary representation '1000010001' and contains two binary gaps: lenghts '4' and '3'. The function should return the maximal gap: '4'.
-- **Example 3:** '20' has binary representation '10100' and contains one binary gap of length '1'. The trailing zeros do not form a gap.
-- **Example 4:** '15' has bianry representation '1111' and has '0' binary gaps.

# 2. Pythonic Solution (String Manipulation)

'''python
def solution(N):
    # Step 1: Convert integer to binary string and strip the '0b' prefix
    binary_str = bin(N)[2:]

    # Step 2: Strip unclosed trailing zeros
    trimmed_binary = binary_str.rstrip("0")

    # Step 3: Split into chunks of zeros separated by '1'
    zero_chunks = trimmed_binary.split("1")

    # Step 4: Determine the maximum sequence length
    max_gap = 0
    for chunk in zero_chunks:
        if len(chunk) > max_gap:
            max_gap = len(chunk)

    return max_gap

---

## 3. Step-by-Step Breakdown

### Step 1: Base Conversion & Slicing ('bin(N)[2:]')
- `bin(N)` converts a positive integer into its binary representation as a string.
- Python prefixes `'ob'` to signify base-2 format (e.g., `bin(9)` becomes `'0b1001'`).
- The slice `[2:]` strips indices 0 and 1, keeping only the raw binary digits `'1001'`.

### Step 2: Stripping Unclosed Trailing Zeros (`.rstrip("0")`)
- By definition, a binary gap must be enclosed by a `1` on both sides.
- Numbers ending with zeros (such as `20 -> 10100` or `32 -> 100000`) have unclosed sequences.
- `.rstrip("0")` removes all consecutive zero from the right edge, ensuring every remaining zero sequence is bounded by `1`s.

### Step 3: Splitting on Delimiters (`.split("1")`)
- `.split("1")` breaks the string at very occurrence of `1`.
- For example. `'1000010001'` becomes `['', '0000', '000', ''].
- Contiguous runs of zeros are isolated as individual strings in a list.

### Step 4: Tracking the Maximum (`max_gap`)
- Initialize `max_gap = 0`.
- Iterate through each string in `zero_chunks` and evaluates its length using `len(chunk)`.
- If `len(chunk) > max_gap`, update `max_gap`.
- Returns `0` automatically if no valid gaps exist.

---

## 4. Complexity Analysis

- **Time Complexity:** $0(\log N)$
  The number of bits in intger $N$ IS $\lfloor \log_2(N) \rfloor + 1$. The functions `bin()`, `rstrip()`, `split()`, and the `for` loop each traverse the bits linearly, resulting in an overall time complexity of $0(\log N)$.
- **Space Complexity:** $0(\log N)$
Coverting the integer into a binary string and storing the resulting chunk list allocates heap memory proportional to the total number of bits.

--

## 5. Critical Edge Cases Handled

| Input ($N$) | Binary Representation | Expected Output | Logic / Reason |
| :--- | :--- | :--- | :--- |
| `1` | `1` | `0` | Smallest valid integer; contains no zeros |
| `15` | `1111` | `0` | All ones; no gaps present |
| `32` | `100000` | `0` | Trailing zeros with no closing `1` |
| `1041` | | `10000010001` | `5` | Two gaps (lengths 5 and 3); returns maximal |
| `2147483647` | $31$ consecutive `1`s | `0` | Maximum 32-bit positive signed integer |

---

## 6. Optimal Bitwise Solution ($0(1)$ Auxiliary Space) while string manipulation is intuitive in Python, interviewers frequently evaluate your ability to solve low-level problems without allocating additional heap memory. The bitwise approachbinary digits directly using bit masks and arithmetic shifts.

### Implementation

```python
def solution_bitwise(N):
    max_gap = 0
    current_gap = 0
    counting = False

    while N > 0 :
        # Extract least significant bit
        bit = N & 1

        if bit == 1:
            if counting:
                if current_gap > max_gap:
                    max_gap = current_gap

            else: 
                # First boundary found; begin gap tracking
                counting = True

            # Reset gap counter on every encountered 1
            current_gap = 0

        else:
            # Increment current gap only if inside an active boundary
            if counting:
                current_gap += 1

        # Shift bits rightwars by 1 position
        N >>= 1

    return max_gap
```

---

### Step-by-Step Bitwise Mechanics

1. **Extracting the Least Significant Bit (`bit = N & 1`):**
  - Applying bitwise AND with `1` isolates the rightmost bit of `N`.
  - If `N` is even, the least significant bit is `0`. If `N` is odd, it is `1`.

2. **The `counting` State Flag:**
  - Trailing zeros (e.g., `32 -> 100000`) do not form a valid gap because they lack a trailing closing `1`.
  - By initializing `counting = False`, all rightmost zeros are ignored until the first `1` bit flips `counting = True`.

3. **Resetting on Boundary ('current_gap = 0'):**
  - Whenever `bit == 1`, any active gap is checked against `max_gap`.
  - `current_gap` is then reset to `0` so the next potential sequemce can be measured independently.

4. **Register Shifting (`N >>= 1`):**
  - The in-place right shift operator moves all bits one position to the right, discarding the bit just evaluated.
  - This executes as single ALU CPU cycle rather than an expensive string slicing or re-allocation operation.

  ---

  ### Method Comparison

  | Metric | String Manipulation Approach | Bitwise Shift Approach |
  | :--- | :--- | :--- |
  | **Time Complexity** | $0(\log N)$ | $0(\log N)$ |
  | **Space Complexity** | $0(\log N)$ (Heap allocation)| $0(1)$ (Constant registers) |
  | **Data Structures** | Strings, Lists (`split`, `rstrip`) | Primitives (`int`, `bool`) |
  | **Best Used For** | Rapid prototyping & Pythonic code | Embedded systems, systems security, hardware constraints |


  ---

  # Codility Lesson 2: Arrays

  ## Problem 1: OddOccurrencesInArray

  ### 1. Problem Description
  A non-empty array `A` consisting of `N` integers is given. The arrray contains an odd number of elements, and each element can be paired another element of the same value, except for one element that is left unpaired.

  - **Goal:** Find and return the unpaired element.
  - **Constraints:**
    - $N$ is an odd integer within the range $[1..1,000,000]$.
    - Each element of array $A$ is an integer within the range $[1..1,000,000,000]$.
    - Time Complexity Target $0(N)$.
    - Space Complexity Target: $0(1)$ auxiliary space.

---

### 2. Optimal Implementation (Bitwise XOR)

```python
def solution(A):
    unpaired = 0
    for number in A:
        unpaired ^= number
    return unpaired
```

---

### 3. Mathematical & Algorithmic Mechanics

Th solution relies on the fundamental algebraic propertiesof the bitwise XOR (`^`) operator:

1. **Identify Property ($X \oplus 0 = x$):**
  - XORing any integer with `0` leaves the integer unchanged.
  - Initialization `unpaired = 0` provides a neutral baseline.

2. **Self-Inverse Property ($X \oplus x = 0$):**
  - Any number XORed with itself produces `0` because matching bit positions result in `0`.
  - Every paired cancels out completely.

3. **Commutative & Associative Properties:**
  - The order of operations does not affect teh final result:
  $$(A \oplus B) \oplus A = (A \oplus A) \oplus B = 0 \oplus B == B$$
  - Regardless of where the duplicate elements are plassed across the array, every duplicate pair evaluates to `0`.

4. **Final Accumulation:**
  - After traversing all elements, all paired numbers collapsa to `0`, leaving only:
   $$\text{unpaired} = 0 \oplus \text{target = \text{target}}$$

   ---

### 5. Architectural Comparison with Alternatives

| Approach | Time Complexity | Space Complexity | Tradeoffs & Limitations |
| :--- | :--- | :--- | :--- |
| **Bitwise XOR Reduction** | $0(N)$ | $0(1)$ | Optimal in both time and memory; handles $10^6$ items natively. |
| **Hash Map / Frequency Counter** | $0(N)$ | $0(N)$ | Requires allocating dynamic heap memeory for up to $N/2$ unique keys. |
| **Sorting (`A.sort()`)** | $0(N log N$)| $0(1)$ to $0(N)$ | Modifies array in place; exceeds $0(N)$ runtime limit on larg arrays. |

---

### 6. Critical Edge Cases Handled

| Input Array (`A`) | Expected Output | Logic / Reason |
| :--- | :--- | :--- |
|`[42]` | `42` | Single-element array; minimum possible odd length ($N = 1$). |
| `[9, 3, 9, 3, 9, 7, 9]` | `7` | Multiple pairs of the same value (`9` appears 4 times); `7` remains unpaired. |
| `[1000, 500, 1000]` | `500` | Symmetrical pairs surrounding the target value. |
| `[1, 2, 3, 2, 1]` | `3` | Odd array with pairs separated across the boundaries. |

## Problem 2: CyclicRotation

### 1. Problem Description
An array `A` consisting of `N` integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. The goal is to rotate array `A` $K$ times.

- **Input Constraints:**
 - $N$ and $K$ are integers within the range $[0 \dots 100]$.
- Each element of array $A$ is an integer within the range $[-1, 000 \dots 1,000]$.

---

### 2. Algorithmic Intution & Mechanical Breakdown

1. **Guard Condition (Zero or Single Elements):**
  - If the array has 0 or 1 element (`len(A) <= 1`), no rotation changes the state, Returning early avoids unnecessary allocations and prevents a `ZeroDivisionError` during modulo arithmetic.
2. **Cycle Optimization ($K \pmod N$):**
  - Rotating an array of length $N$ by $N$ times results in the original array.
  - When $K \ge N$. effective shifts equal `k = K % N`. If `k == 0`, the array reamins identical.
3. **Array Slicing:**
  - The last `k` elements move to the front: `A[-k:]`.
  - The first `N - k` elements follow: `A[:-k]`.
  - Result: `A[-k:] + A[:-K]`.

---

### 3. Complexity Matrix

| Metric | Complexity | Rationale|
| :--- | :--- | :---|
| **Time Complexity** | **$0(N)$**| Modulo arithmetic is $0(1)$. Slicing and concatenating two sublists requires shallow copying $N$ references. |
| **Space Complexity*| **$0(N)$**| A new list of length $N$ is created and returned to fulfil the  Codility interface requirement. Auxiliary memory is $0(1)$. |

--- 4. Critical Edge Cases Tested

| Test Case | Input `(A, K)` | Expected Output | Mechanical Significance |
| :--- | :--- | :--- | :--- |
| **Standard Shift** | `([3, 8, 9, 7, 6]), 3` | `[9, 7, 6, 3, 8]` | Standard multi-shift validation |
| **Identical Elements** | `([0, 0, 0], 1)` | `[0, 0, 0]` | Value equality verification |
| **Full Cycle ($K = N$)** | `([1, 2, 3, 4], 4)` | `[1, 2, 3, 4]` | Verifies $4 \pmod 4 = 0$ returns unchanges list |
| **Empty Array** | `([], 5)` | `[]` | Prevents `ZeroDivsionError` (`5 % 0`) |
| **Single Elements** | `([1], 99)` | `[]` | Validates $K \gg N$ edge behavior |
| **Oversized Shift ($K > N$)** | `([1, 2], 3)` | `[2, 1]` | Confirms $3 \pmod 2 = 1$ reduction |
| **Zero Shift ($K = 0$)** | `([1, 2, 3, 4, 5], 0)` | `[1, 2, 3, 4, 5]` | Verifies immediate no-op return |
| **Negative Values** | `([-1, -2, -3, -4], 2)` | `[-3, -4, -1, -2]` | Ensures signs do not corrupt slicing indexes |

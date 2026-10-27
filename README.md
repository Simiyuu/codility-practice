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
  


            
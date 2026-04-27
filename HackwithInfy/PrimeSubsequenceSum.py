"""
## Q3 Prime Subsequence Sum

**10 marks | 3s limit | 256MB**

### Problem Statement
You are given an array **A** of **N** positive integers. You need to find the **number of non-empty subsequences** of the array such that the **sum of the subsequence is a prime number**.

Since the answer can be very large, print it modulo $10^9 + 7$.

### Definitions
* A **subsequence** is a sequence derived from the array by deleting zero or more elements without changing the order of remaining elements.
* A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Input Format
* First line contains a single integer **N**.
* Second line contains **N** space-separated integers representing array **A**.

### Output Format
* Print a single integer — the count of subsequences with prime sum, modulo $10^9 + 7$.

---

### Examples

#### Example 1
**Input:**
```
3
1 2 3
```
**Output:**
```
4
```
**Explanation:** All non-empty subsequences:
* `[1]` sum = 1 (not prime)
* `[2]` sum = 2 (prime)
* `[3]` sum = 3 (prime)
* `[1, 2]` sum = 3 (prime)
* `[1, 3]` sum = 4 (not prime)
* `[2, 3]` sum = 5 (prime)
* `[1, 2, 3]` sum = 6 (not prime)
**Count = 4.**

#### Example 2
**Input:**
```
4
2 2 2 2
```
**Output:**
```
4
```
**Explanation:** Only sum 2 is prime, achieved by 4 single-element subsequences.

#### Example 3
**Input:**
```
2
1 1
```
**Output:**
```
1
```
**Explanation:** Only `[1, 1]` has prime sum 2.

---

### Note
* Two subsequences are different if they differ in at least one index.
* 1 is **NOT** a prime number.
* 2 is the smallest prime number.

### Constraints
* $1 \le N \le 1000$
* $1 \le A[i] \le 1000$
* Sum of array $\le 10^6$
* **Time Limit:** 3 seconds
* **Memory Limit:** 256 MB
"""
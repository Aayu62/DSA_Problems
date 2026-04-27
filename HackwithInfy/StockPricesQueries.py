"""
## Q2 Stock Price Queries

**10 marks | 3s limit | 256MB**

### Problem Statement
You are analyzing stock prices over **N** days. The price on day $i$ is $P[i]$. You need to process **q** queries of two types:

1.  **Update Query (Type 1):** `1 i x` — Update the price on day $i$ to $x$.
2.  **Range Query (Type 2):** `2 l r` — Find the **maximum profit** that could be made by buying on some day $b$ and selling on some day $s$ where $1 \le b < s \le r$.

The profit is $P[s] - P[b]$. You must buy before selling ($b < s$).

If no profit is possible (all prices are non-increasing in the range), output **0**.

### Input Format
* First line contains two space-separated integers **N** and **Q**.
* Second line contains **N** space-separated integers representing prices $P[1], P[2], \dots, P[N]$.
* Next **Q** lines each contain a query.

### Output Format
* For each Type 2 query, print the maximum profit on a new line.

---

### Examples

#### Example 1
**Input:**
```
5 4
3 1 4 1 5
2 1 5
2 2 4
1 3 2
2 1 5
```
**Output:**
```
4
3
4
```
**Explanation:**
* Query 1: Range $[1, 5] = [3, 1, 4, 1, 5]$. Buy at day 2, sell at day 5. Profit = 4.
* Query 2: Range $[2, 4] = [1, 4, 1]$. Buy at day 2, sell at day 3. Profit = 3.
* After update, array is $[3, 1, 2, 1, 5]$.
* Query 3: Range $[1, 5]$. Buy at day 2 or 4, sell at day 5. Profit = 4.

#### Example 2
**Input:**
```
4 3
5 4 3 2
2 1 4
1 4 10
2 1 4
```
**Output:**
```
0
7
```
**Explanation:**
* Range $[1, 4] = [5, 4, 3, 2]$. Decreasing, no profit. Output 0.
* After update: $[5, 4, 3, 10]$. Buy day 3, sell day 4. Profit = 7.

---

### Note
* Days are 1-indexed.
* You must buy strictly before selling.

### Constraints
* $1 \le N, Q \le 10^5$
* $1 \le P[i], x \le 10^9$
* $1 \le i \le N$
* $1 \le l < r \le N$
* **Time Limit:** 3 seconds
* **Memory Limit:** 256 MB
"""
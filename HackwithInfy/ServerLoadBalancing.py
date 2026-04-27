""" 
Problem StatementYou are managing a data center with N tasks that need to be assigned to K servers. 
Each task $i$ has a processing load of $L[i]$ units.Tasks must be assigned in contiguous groups to servers. 
That is, you partition the array of tasks into K contiguous segments, and each segment is assigned to one server.
The load on a server is the sum of processing loads of all tasks assigned to it. 
You want to minimize the maximum load on any server.Find the minimum possible value of the maximum load on any server.

Input Format: First line contains two space-separated integers N and K.
Second line contains N space-separated integers representing loads $L[1], L[2], \dots, L[N]$.

Output Format: Print a single integer — the minimum possible maximum load on any server.Examples

Example 1
Input:5 2
1 2 3 4 5
Output:9
Explanation: Optimal partition: $[1, 2, 3]$ and $[4, 5]$Server 1: $1 + 2 + 3 = 6$Server 2: $4 + 5 = 9$Maximum load = $9$.


Example 2
Input:6 3
10 20 30 40 50 60
Output:90
Explanation: Optimal partition: $[10, 20, 30], [40, 50], [60]$Server loads: $60, 90, 60$Maximum load = $90$.Example 3Input:4 4
100 200 300 400
Output:400
Explanation: Each task gets its own server. Maximum load = $\max(100, 200, 300, 400) = 400$.NoteAll tasks must be assigned.Tasks must maintain their order (contiguous assignment).Constraints$1 \le K \le N \le 10^5$$1 \le L[i] \le 10^9$Time Limit: 2 secondsMemory Limit: 256 MB
"""

import sys

def can_assign(loads, k, max_load):
    server_count = 1
    current_load = 0
    for load in loads:
        if current_load + load > max_load:
            server_count += 1
            current_load = load
        else:
            current_load += load
    return server_count <= k

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    n = int(line1[0])
    k = int(line1[1])
    
    # Reads the second line (Loads)
    line2 = sys.stdin.readline().split()
    if not line2: return
    loads = list(map(int, line2))

    low = max(loads)
    high = sum(loads)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_assign(loads, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)

if __name__ == "__main__":
    solve()
#!usr/bin/env python 3


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[]  of  integers each separated by a space.

# Constraints
#2<=n<=10
#-100<=A[i]<=100

# Output Format
# Print the runner-up score.

# Sample Input 0
# 5
# 2 3 6 6 5

# Sample Output 0
# 5

# Explanation 0
# Given list is [2,3,6,6,5]. The maximum score is 5, second maximum is 5. Hence, we print  as the runner-up score.


n = int(input())
arr = list(map(int,input().split()))
done = max(arr)
while max(arr) == done:
      arr.remove(max(arr))
print(max(arr))


#!urs/bin/env python3

# Read an integer N.

# Without using any string methods, try to print the following:
# 123....N

# Note that "" represents the values in between.

# Input Format

# The first line contains an integer N.

# Output Format

# Output the answer as explained in the task.

# Sample Input 0

# 3
# Sample Output 0

# 123

n=int(input())
for x in range(1,n+1,1):
  print(x,end="")

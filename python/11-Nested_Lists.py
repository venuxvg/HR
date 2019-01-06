#!usr/bin/env python 3


# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, , the number of students. 
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

# Constraints
#2<=N<5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2  belongs to Tina. The second lowest 37.2 grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


n=int(input())
arr=[]
for i in range(0, n):
    str1 = input()
    str2 = float(input())
    str3= [str1,str2]
    arr.append(str3)
m=len(arr)
filtered=[]
for x in range(0,m):  
  second=arr[x][1]
  filtered.append(second)
filtered.sort()
rea=min(filtered)
while min(filtered) == rea:
      filtered.remove(min(filtered))
# print(min(filtered))
l=len(arr)
names=[]  
for i in range(0,l):
  if (min(filtered)==arr[i][1]):
    first=arr[i][0]
    names.append(first)
names.sort()
l2=len(names)
for k in range(0,l2):
  print(names[k])

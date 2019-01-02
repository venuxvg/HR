#!/usr/bin/env python3

#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird
#Input Format

#A single line containing a positive integer, .

#Constraints
#1<=n<=100

#Output Format
#Print Weird if the number is weird; otherwise, print Not Weird.

#Sample Input 0
#3

#Sample Output 0
#Weird


#Explanation 0
#n=3
#n is odd and odd number are wierd,so we print Weird 

#Sample Input 1
#24

#Sample Output 1
#Not Weird

#Explanation 1

#n=24 
#n>20 and n is even, so it isn't weird. Thus, we print Not Weird.


N = int(input())
if 1<=N<=100:
    if N%2:
        print("Weird")
    else:
        if N>=2 and N<=5:
            print("Not Weird")
        else:
            if N>=6 and N<=20:
                print("Weird")
            else:
                print("Not Weird")

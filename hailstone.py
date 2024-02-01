# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/31/2024
# Description: Project 4c

def hailstone(n):
    count = 0  # number of steps to 0
    while n != 1:  # as long as n is not 1
        if n % 2 == 0:  # if n is even
            n //= 2
        else:
            n = 3 * n + 1
        count += 1  # increase number of steps by 1
    return count  # return the number of steps it took
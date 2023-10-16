# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:35:24 2023

@author: 91635
"""

from itertools import permutations

def check_per(ans, a, ip, i):
    input_queue = list(ip)
    output_queue = list(a[i])
    temp_stack = []

    while input_queue:
        e = input_queue.pop(0)
        if e == output_queue[0]:
            output_queue.pop(0)
            while temp_stack and temp_stack[-1] == output_queue[0]:
                temp_stack.pop()
                output_queue.pop(0)
        else:
            temp_stack.append(e)

    if not input_queue and not temp_stack:
        ans.append(i)
        return True
    else:
        return False

def main():
    n = int(input("Enter the number: "))
    
    if n < 1:
        print("Invalid input. Please enter a positive integer.")
        return

    #ip = list(range(1,n+1))
    ip = list(range(n, 0, -1))  # Generate a list in decreasing order from n to 1
    v = list(permutations(ip))
    ans = []

    for i in range(len(v)):
        check_per(ans, v, ip, i)

    print(f"Total permutation possible: {len(ans)}")

    for i in ans:
        print(*v[i])

if __name__ == "__main__":
    main()

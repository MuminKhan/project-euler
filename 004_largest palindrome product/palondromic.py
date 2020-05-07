#!/bin/python3

###################################################################################
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Write a function to find the largest palindrome made from the product of two 3-digit numbers.
# 
# Ans: 906609
###################################################################################

def is_numeric_palindrome(num):
    num = str(num)
    return num == num[::-1]

def find_palindrome(digits = 3, limit = -1):
    small = 10 ** (digits - 1)
    big =  (10 ** digits) - 1

    largest_palindrome = 0
    products = [0, 0]

    for i in range(big, small, -1):
        if i * i < largest_palindrome:
            break

        for j in range(i, small, -1):
            product = i*j

            # This is for Hackerrank's version
            if limit > 0 and product >= limit: 
                continue

            if is_numeric_palindrome(product) and product > largest_palindrome:
                products = [i,j]
                largest_palindrome = product
                
    #print(products)
    return(largest_palindrome)   

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    find_palindrome(3, n)
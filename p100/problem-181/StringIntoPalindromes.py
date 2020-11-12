# This problem was asked by Google.
#
# Given a string, split it into as few strings as possible such that each string is a palindrome.
#
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
#
# Given the input string abc, return ["a", "b", "c"].

#GOOGLE
#DP
# GG: This took a lot of effort for even the naive solution, and I don't have the back tracking done yet.
# TBC
"""
Not sure where to start at first. This smells like a dynamic programming problem though

As few as possible, aka, each of the palindrome should be as big as possible.

Given a string, worst case is it will be split up to n palindromes, where each is one character long.

After half an hour of doodling, I think we need two 2D array.
p(i, j) is True if substring i..j is a palindrome
c(i, j) is how many minimum palindrome needed to cover this substring

p(i, j) = {
    True if i = j and p(i +1, j-1) is True
    False otherwise
}

Then
c(i, j) = {
    1 if p(i, j) is True
    min( c(i, m) + c(m+i, j)) where i < m < j
}

This would get me the minimum num of palindrome needed, but I guess I have to back trace, or modify the code to find the
individual palindromes
"""
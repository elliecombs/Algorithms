'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?'''

'''STEPS #Inputs clarification (integers or empty array, different data type)
#Outputs (integers or empty array, different data type)
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#Example Setup (if not provided or code out your own)
#Pseudo Code:
#Time & space Complexity:'''

#O(n) Time & Space Complexity 
#Solution 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Initialize pointers i & j at zero 
        i, j = 0, 0

        #Run loop while both pointers are inbound, each must be less than the length of # of elements
        while i < len(s) and j < len(t):
            #Conditions
            if s[i] == t[j]:
                #Increment/shift i & j
                i += 1
            #j will always be incremented no matter the comparison
            j += 1
        #for every character in s we are able find a matching character in t then return true, if not the case we return false and loop ended j went out of bounds for t
        return True if i == len(s) else False
    

#Compare string s and t, iterate through each array at the same time, first array must be less then the second & the second array
#Initialize i for s and j for t to 0 index
#Iterate through each element of the arrays at the same time for their length and compare if it is in the other string
#Time&Space Complexity:  O(2n) or O(n+n)
#Using 2 pointers , only shift if the letter isn't there and once i pointer is out of bounds we found the solution!
#Linear Time
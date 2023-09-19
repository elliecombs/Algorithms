'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''


'''OWN EXAMPLES
s = "alsahf"
t = "ambtre"
output = True
    Length of letters- asfd oij False
        Arranging letter order hut tuh True
        2 of the same letters tuppt tputp tpuuu True
        All different letters obx xbo True

STEPS
step 0.5: if len of s != len of t, return False
step 1: create a hash map for s
step 2: create a hash map for t
step 3: check all characters along with their counts
step 4: true or false'''

#Solution 1
class Solution:
    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        hashMapS, hashMapT = {}, {}
        for ch in s: # ch = 'l', hashMapS = {a:2, l:1, s:1}
            if ch in hashMapS:
                hashMapS[ch] += 1
            else:
                hashMapS[ch] = 1

        for ch in t:
            if ch in hashMapT:
                hashMapT[ch] += 1
            else:
                hashMapT[ch] = 1

        for key in hashMapS.keys():
            if hashMapS[key] != hashMapT.get(key, 0):
                return False

        return True

#Solution 2
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            #Another solution with just this line by sorting
            # return sorted(S) == sorted(t)
            
            #Check if the length of the strings are the same
            if len(s) != len(t):
                return False

            #Count characters in both strings
            countS, countT = {}, {}

            #Go thru length of the strings at same time- i
                #Occurrence of each character for S & T at index i
                # Increment character by 1- must add get (the key- countS[s[i]]) and 0 for default value if character doesn't exist yet. Get stops key error as we need to get the key!
                #Iterate through hashmaps with c
                #Overall build hashmap with i then check with c
                #Time/Space Complexity O(n) or O (s+t) also nlogn for quickest solution with sorting
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            for c in countS:
                if countS[c] != countT.get(c,0):
                    return False
                
            return countS == countT
        
            # return True
            # Option long format
            # for c in countS:
            #     if countS[c] != countT.get(c,0):
            #         return False
                # return True
            
            # Option Python Specific short format, counts automatically and set exactly equal to each other True if not False
            # or Counter(s) == Counter(t)
            
            #Solution using O(n), sorted order 
#Solution 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
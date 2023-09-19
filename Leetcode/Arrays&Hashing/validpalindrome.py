'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''

#Ignoring upper and lower cases, considering only alphanumeric characters, 0-9, a-z & A-Z, 
#Must read same way forward and reversed (example aba yes)

#Remove spaces/special character and converting to lower case -> reverse string must be same string as read forward
#Solution uses more memory & built in Python functions
#Solution 1
Class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Remove non alpha-numeric characters
        newStr = ""

        #Itreate through each character in string S
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        newStr == newStr[::-1]
        
#Solution using pointers (Left & Right)
#Compare l & r characters and see if they are equal (decrementing r & incrementing l) until meet in middle or left passes right pointer to stop (depending on odd or even amount of characters)
#Use Ascii numbers ()associated with values

##Solution 2
Class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Right side starting at 0, length of string - 1
        1 r = 0, len(s) - 1
            #Left is less than the right pointer, this is Left
            while 1 < r:
                #L & R must be alphanumeric, Left
                while 1 < r and not alphaNum(s[1]):
                    1 += 1
                #Right
                while r > 1 and not alphaNum(s[r]):
                    r -= 1
                #Character at position left & right if not equal return False only use lowercase versions
                if s[1].lower() != s[r].lower():
                    return False
                #After comparison update l & r pointers to next position
                1, r = 1 + 1, r - 1
            return True

        #function for alpha num checking
        def alphaNum(self, c):
            #Is it an upper case character using Ascii
            return (ord('A') <= ord('Z') or
                    ord('a')) <= ord('z') or
                    ord('0')) <= ord('9'))
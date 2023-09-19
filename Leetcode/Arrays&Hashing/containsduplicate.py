'''
CONTAIN DUPLICATE HASH
Can use sort or Hash

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
# [1 2 3] - Check/keep track if variable is in the hashset - O(1)
    # Key take away: whenever you need to access or check if something exists - use a hashset
    #O(n) Time & Space complexity
    
    # hashset - check if its in there O(1)
    #         - remove O(1)
    #         - add O(1)

    #           array to check: O(n) -> not the optimal solution takes to long
    #containsDuplicate = function
    #Solution = Object
    #Self references everything in class, nums is the variable: datatype is list of integers
    #Bool containsDuplicate(ArrayList<int> nums) in Java -> Best practice to write this out so others know, (Python isn't typed so this function would work without this line)
    #Throwing each item one at a time into hash to check if it already exists or not (1 item only & must be unique) if it is true then we add it in and if not then it is false
    #O(n) n = length of the array (uses extra space/memory but run time was good!)
    
#SOLUTION 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    #Does the array have a duplicate number? If yes return true if no return false!
    #Use a hashset to find if there is a duplicate value
    #Iterate through the array one element at a time
    #Hashset checks each number in the array i 
    #Return True or False
    #O(n) Time Complexity: there's only 1 iteration for the length array

#SOLUTION 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    #set(nums) Python specific takes in each number
    #len Counts how many nums in unique hashset, automatically removes duplicate *python specific function 3 in this case
    #len(nums) Counts how many in original array 4 in this case
    #Checks if the num from the first & second list are the same or not
    #Runs true for a duplicate or false none
    #O(n) Time Complexity
    #Linear, each for loop is independent, 
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? '''
#Looking for 4-1 difference between value and target, value each # in array and target is 4
#Time complexity iterating once constant time O(n) hashmap not free O(n)

#Solution 1
class Solution:
    def twoSum(self, nums, target: int):
        #Represents every element that comes before the map 
        #prevMap Val : index (comparing value to index of that value)
        prevMap = {}  #val : index

        #Must iterate through every index in the array
        for i, n in enumerate(nums):
            #Check for difference & if it is already in the hashmap
            diff = target- n
            if diff in prevMap:
                #if yes get pair of indicies 
                return [prevMap[diff], i]
            #If not then update hashmap and go through function again
            prevMap[n] = i

obj = Solution()
nums = [4,1,-1,9,0,2]
target = 5 
print(obj.twoSum(nums, target))

#Solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        findtargetlist = {}
        for i in range len(nums):
            n = nums[i]
            diff = target - n 
            if diff in findtargetlist:
                return [findtargetlist[diff], i]
            findtargetlist[i] = n

#Return the INDICES of 2 numbers that add up to the target number. Each input has 1 solution only. No using the same element twice.
#Create/define a list -> iterate through that list for the length of the numbers (use indicies not value)
#Calculate difference between numbers by target - n 
#Time Complexity Solution 1 & 2 O(n)

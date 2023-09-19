'''Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000'''

#Solution 1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        #Wrap in another outer loop to execute 2 times
        for i in range(2):
            
            #For every number in nums append n to answer
            for n in nums:
                ans.append(n)
            return ans

#Solution 2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums 

#Concatenate (combine 2 strings). Create an array called ans with length 2n and by index return ans. 
#Create an empty list to store the elements in the array repeated twice.
#Iterate through the loop.
#Append to the ans and return
#Space Complexity & Time Complexity Solution 1 O(N+N) Solution 2 O(n)
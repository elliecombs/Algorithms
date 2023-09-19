'''Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105'''

'''STEPS #Inputs clarification (integers or empty array, different data type)
#Outputs (integers or empty array, different data type)
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#Example Setup: (if not provided or code out your own)
#Pseudo Code:
#time & space Complexity O(M+N) O (mlogm +nlogn)sort function, O(1) or O(m+n) creating new list'''

#Solution 1
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastindx = -1
        for i in range (len(arr) - 1, -1, -1):
            newmax = max(lastindx, arr[i])
            arr[i] = lastindx
            lastindx =  newmax
        return arr

#Inputs clarification (integers or empty array, different data type)
#Outputs (integers or empty array, different data type)
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#Example Setup: in VS Code
#Pseudo Code: iterate through arr -> replace each index to right and end with -1, output - 1
#Setting the last index to -1, iterate through the len of the arr, start point is -1, stop value stops loop, going from right to left -1 
#Assign new maximum after comparing diff elements in the array
#time & space Complexity O(n) searching

#Initial max = -1
#Reverse iteration (compare to see which element is higher), stop once at beginning of arr 
#New max = max(oldmax, arr[i]) is old max + previous position in the arr 
#Overwrite value & update current right max with what we just computed 

#Solution 2
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #Initial Max, last value to be replaced 
        rightMax = -1
        
        #Reverse Iteration
        #newMax = max (oldmax, arr[i]) is old max & previous position in array
        
        #each -1: start at last value in array, iterate reverse order, stop once at beginning of array
        for i in range(len(arr) - 1, -1, -1):
            
            #Replace current value w/right max
            newMax = max(rightMax, arr[i])
            
            #overwrite value
            arr[i] = rightMax
            
            #Update current right max with current max just computed 
            rightMax = newMax
        return arr
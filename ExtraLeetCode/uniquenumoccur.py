'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true'''

#Solution 1
#The comparison checks whether the number of unique elements in arr is equal to the number of unique frequencies in the counts. If they are equal, it means that all frequencies are unique, so the function returns True, indicating that all occurrences are unique. Otherwise, it returns False.

#In summary, this code uses the collections.Counter class to efficiently count the occurrences of elements in the input list arr. Then, it checks whether the number of unique elements and the number of unique frequencies are the same. If they are, it returns True; otherwise, it returns False.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        #Count occurrences of elements in input list arr
        #Creates dict like object c where keys are unique elements from arr and values are corresponding counts to each element
        c = collections.Counter(arr)      
        
        #Calculates 2 lengths and compares them
        #Unique elements in c object corresponding to number of unique elements in input list arr
        #Calculates number of unique values in the c object (Extracts all values from obj c, counts each element then converts into set and deletes duplicates and finally calculates length of set)
        return len(c) == len(set(c.values()))
    
#Solution 2  
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #Create an empty dictionary 
        hashmap = {}
        
        #Iterate over indicies of the elements in arr list
        for i in range(len(arr)):
            
            #Checks if element arr[i] is already a key in hashmap
            if arr[i] in hashmap:
                
                #If already in hashmap, increment associated value in dictionary by 1
                hashmap[arr[i]] += 1
            else:
                #If not in hashmap, create new entry in hm as key and set value 1
                hashmap[arr[i]] = 1
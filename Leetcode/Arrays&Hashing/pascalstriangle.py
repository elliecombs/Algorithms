'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]'''

#Solution 1
class Solution:
    def generate(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        else:
            return self.getAllRow(rowIndex - 1)

    def getAllRow(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        ListPrec = self.getAllRow(rowIndex - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec
        
Input = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#Variable name set to the class
solution = Solution()
#Run generate method (call object the access method)
print(solution.generate(Input))


#Inputs clarification (integers or empty array, different data type)
#Posative integers in this case
#Outputs (integers or empty array, different data type)
#Posative integers or empty array
#Non decreasing- might have duplicates but won't decrease
#Potential Edge Cases & examples: (no negatives, null, floating point etc)
#if M = 2, what about 2nd index? or anything after? Modify to zero?
#Example Setup
#Pseudo Code: num1 take index 0-2, slice function python and store as num1, next sort in non-decreasing order,
#Test Manual or compiler
#time & space Complexity O(n)2 

#Solution 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initialize the list that will store the rows of Pascal's Triangle
        ans = [] 

        # outer loop to iterate for the number of rows specified
        for i in range(numRows):
            # initialize a list to store the current row
            row = []

            # inner loop to iterate for each element in the current row
            #j is number of elements in each row, i is index in a whole row
            # Add 1 from row above both left & right because of Ptriangle characteristic
            for j in range(i + 1):

                # check if the current element is the first or the last in its row
                if j == 0 or j == i:
                    # append 1 to the row list since the first and last elements are always 1
                    row.append(1)
                else:
                    # calculate the current element by adding the two elements in the previous row directly above it
                    # append the result to the row list
                    #Forming the triangle / center output
                    row.append(ans[i - 1][j - 1] + ans[i - 1][j])

            # after all elements in the current row have been computed, append the row list to the ans list
#             ans.append(row)
#         # after all rows have been computed, return the ans list which now contains the first numRows rows of Pascal's Triangle
#         return ans

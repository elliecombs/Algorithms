'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.'''

input = strs =

                  i 
                        j
output = [["eat","tea","ate"], ["nat", "tan"], ["bat"]]
             t. a. e 
  
  #Clarify inputs: array strings
  #Output: array of strings
  #Edgecases: no
  #Take inputs and check if they're anagrams, by checking one element compared other indicies in the whole array
  #Sorts or stores the ones that are matching anagrams in different 'buckets'
  
def groupingAnagrams(strs)
  anagrams = []
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if len(strs[i]) = len(strs[j])
        if 
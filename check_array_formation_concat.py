# You are given an array of distinct integers arr and an array of integer arrays pieces, where the 
# integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in 
# any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

#----- Example 1:-----:

# Input: arr = [85], pieces = [[85]]
# Output: true



class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {piece[0]: piece for piece in pieces}
        res = []
        for i in arr:
            res += mapping.get(i, [])
            
        return res == arr
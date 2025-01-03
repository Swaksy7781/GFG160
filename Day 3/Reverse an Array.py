class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        start = 0
        end = n-1
        
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
        return arr
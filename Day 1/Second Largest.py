class Solution:
    def getSecondLargest(self, arr):
        
        if len(arr) < 2:
            return -1
        
        maxi = -1
        second_maxi = -1
        
        for i in range(len(arr)):
            if arr[i]>maxi:
                second_maxi = maxi
                maxi = arr[i]
            elif arr[i] > second_maxi and arr[i] != maxi:
                second_maxi = arr[i]
        return second_maxi

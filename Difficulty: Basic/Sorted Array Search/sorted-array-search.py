#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        n = len(arr)
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return False
                
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends
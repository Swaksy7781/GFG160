class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1  # Calculate the expected length of the array
        expected_sum = n * (n + 1) // 2  # Calculate the sum of numbers from 1 to n
        actual_sum = sum(arr)  # Calculate the sum of the given array
        return expected_sum - actual_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends
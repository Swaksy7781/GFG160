class Solution:
    def maxSubArraySum(self,arr):
        """
        Finds the maximum sum of a contiguous subarray in the given array.

        Args:
            arr: The input array of integers.

        Returns:
            The maximum sum of a contiguous subarray.
        """
        max_so_far = arr[0]
        curr_max = arr[0]

        for i in range(1, len(arr)):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
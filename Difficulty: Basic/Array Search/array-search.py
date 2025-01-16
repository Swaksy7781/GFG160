class Solution:
    def search(self, arr, x):
        """
        Finds the index of the first occurrence of 'x' in the array 'arr'.

        Args:
            arr: The input array of integers.
            x: The element to be searched.

        Returns:
            The index of the first occurrence of 'x' in 'arr', or -1 if 'x' is not found.
        """
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        x = int(input())
        ob = Solution()
        print(ob.search(A, x))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
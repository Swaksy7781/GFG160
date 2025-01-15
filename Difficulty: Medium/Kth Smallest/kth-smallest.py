#User function Template for python3
class Solution:
    def kthSmallest(self, arr, k):
        """
        Finds the kth smallest element in the given array.

        Args:
            arr: The input array.
            k: The index of the kth smallest element (1-indexed).

        Returns:
            The kth smallest element in the array.
        """

        # Find the maximum element in the array
        max_element = max(arr)

        # Create a count array to store the frequency of each element
        count = [0] * (max_element + 1)

        # Count the occurrences of each element
        for num in arr:
            count[num] += 1

        # Find the kth smallest element by iterating through the count array
        kth_smallest = 0
        for i in range(max_element + 1):
            kth_smallest += count[i]
            if kth_smallest >= k:
                return i



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends
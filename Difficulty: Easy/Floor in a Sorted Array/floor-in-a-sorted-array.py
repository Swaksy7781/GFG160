class Solution:
    def findFloor(self, arr, k):
        
        if k < arr[0]:
            return -1

        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == k:
                return mid

            if arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1

        return end
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
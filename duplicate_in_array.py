class Solution:
    def duplicates(self, arr, n):
        result = set()
        seen = set()

        for num in arr:
            if num in seen:
                result.add(num)
            else:
                seen.add(num)

        result = sorted(list(result))  # Convert the set back to a sorted list

        if not result:
            result.append(-1)

        return result
#{
# Driver Code Starts 
if (__name__ == '__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution.duplicates(arr, n)
        for i in res:
            print(i, end=" ")
        print()

#} Driver Code Ends

class Solution():
    def third(self, nums):
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        if len(seen) < 3:
            return max(seen)
        else:
            third = list(seen)
            third.sort(reverse=True)
            return third[2]

def main():
    nums = list(map(int, input("enter the numbers: ").split()))
    s = Solution()
    third = s.third(nums)
    print("the third maximum number is ", third)

if __name__ == "__main__":
    main()
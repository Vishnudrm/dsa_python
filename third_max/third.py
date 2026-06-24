class Solution():
	def third(self,nums):
		first=float("-inf")
		second=float("-inf")
		third=float("-inf")
		for i in range(len(nums)):
			if nums[i]<third:
				continue
			if nums[i]==first or nums[i]==second or nums[i]==third:
				continue
			elif nums[i]>first:
				third=second
				second=first
				first=nums[i]
			elif nums[i]>second:
				third=second
				second=nums[i]
			else :
				third=nums[i]
		if third==float("-inf"):
			return first
		return third
def main():
	nums=list(map(int,input("enter the numbers:").split()))
	s=Solution()
	third=s.third(nums)
	print("the third maximum number is ",third)
	
if __name__=="__main__":
	main()

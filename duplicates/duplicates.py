class Solution():
	def duplicates(self,nums):
		seen=set()
		for i in range(len(nums)):
			if nums[i] in seen:
				return True
			else:
				seen.add(nums[i])
		return False
			


def main():
	nums=list(map(int,input("enter the numbers in the array:").split()))
	s=Solution()
	dupli=s.duplicates(nums)
	print(dupli)
	
if __name__=="__main__":
	main()

class Solution():
	def sum(self,nums,target):
		seen={}
		for i in range(len(nums)):
			complement=target-nums[i]
			if complement in seen:
				return [seen[complement],i]
			else:
				seen[nums[i]]=i
def main():
	nums=list(map(int,input("enter the numbers in the array:").split()))
	target=int(input("enter the target:"))
	s=Solution()
	index=s.sum(nums,target)
	print("the indices are:",index)

if __name__=="__main__":
	main()

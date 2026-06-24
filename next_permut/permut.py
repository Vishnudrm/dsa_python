class Solution():
	def next(self,nums):
		pivot=-1
		for i in range(len(nums)-2,-1,-1):
			if nums[i]<nums[i+1]:
				pivot=i
				break
		if pivot==-1:
			return nums.reverse()
		for i  in range(len(nums)-1,pivot,-1):
			if nums[i]>nums[pivot]:
				nums[i],nums[pivot]=nums[pivot],nums[i]
				break
			
		left=pivot+1
		right=len(nums)-1
		
		while left<right:
			nums[left],nums[right]=nums[right],nums[left]
			left+=1
			right-=1
		return nums
				
			
def main():
	array=list(map(int,input("enter the elements in the array:").split()))
	s=Solution()
	next=s.next(array)
	print("the next permuted array is ",next)

if __name__=="__main__":
	main()

class Solution():
	def jumps(self,nums):
		farthest=0
		end=0
		jump=0
		for i in range(len(nums)-1):
			farthest=max(farthest,i+nums[i])
			if i ==end:
				jump+=1
				end =farthest
		return jump

def main():
	nums=list(map(int,input("enter the elements:").split()))
	s=Solution()
	jump=s.jumps(nums)
	print("the number of jumps is:",jump)
	
if __name__=="__main__":
	main()

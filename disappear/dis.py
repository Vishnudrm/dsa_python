class Solution():
	def dis(self,nums):
		output=set(nums)
		out=[]
		for i in range(1,len(nums)+1):
			if i not in output:
				out.append(i)

		return out 


def main():
	nums=list(map(int,input("enter the numbers:").split()))
	s=Solution()
	dis=s.dis(nums)
	print("disappeared numbers:",dis)



if __name__=="__main__":
	main()

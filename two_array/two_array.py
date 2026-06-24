class Solution():
	def inter(self,nums1,nums2):
		result=set()
		seen=set(nums1)
		for i in range(len(nums2)):
			if nums2[i] in seen:
				result.add(nums2[i])
		return list(result) 

def main():
	nums1=list(map(int,input("enter the first list:").split()))
	nums2=list(map(int,input("enter the second list:").split()))
	s=Solution()
	intersection=s.inter(nums1,nums2)
	print("intersection of 2 arrays ",intersection)

if __name__=="__main__":
	main()

class Solution:
	def intersect(self, nums1, nums2):
		result=[]
		for i in range(len(nums2)):
			if nums2[i] in nums1:
				result.append(nums2[i])
				nums1.remove(nums2[i])
		return result

def main():
	nums1=list(map(int,input("enter the elements in the list:").split()))
	nums2=list(map(int,input("enter the elements in the list:").split()))
	s=Solution()
	intersect=s.intersect(nums1,nums2)
	print("the intersecting number is ",intersect)
if __name__=="__main__":
	main()

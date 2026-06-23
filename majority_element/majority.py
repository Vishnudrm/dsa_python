class Solution():
	def majority(self,elements):
		candidate=elements[0]
		count=1
		for i in range(1,len(elements)):
			if count==0:
				candidate=elements[i]
				count=1
			elif elements[i]==candidate:
				count+=1
			else:
				count-=1
		return candidate	

def main():
	elements=list(map(int,input("enter the elements in the list: ").split()))
	s=Solution()
	major=s.majority(elements)
	print("the majority element is ",major)
if __name__=="__main__":
	main()

class Solution:
    def majorityElement(self, elements):
        count={}
        for i in range(len(elements)):
            if elements[i] in count:
                count[elements[i]]+=1
            else:
                count[elements[i]] = 1  
        return max(count,key=count.get)
		
def main():
	elements=list(map(int,input("enter the elements in the list: ").split()))
	s=Solution()
	major=s.majorityElement(elements)
	print("the majority element is ",major)
if __name__=="__main__":
	main()
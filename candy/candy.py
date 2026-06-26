class Solution():
	def maximum(self,candies):
		sets=set(candies)
        
		return min(len(sets),(len(candies))//2)
def main():
	candies=list(map(int,input("enter the types of candies:").split()))
	s=Solution()
	candies=s.maximum(candies)
	print("maximum number of candies:",candies)
	
if __name__=="__main__":
	main()

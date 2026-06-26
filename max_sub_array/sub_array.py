class Solution():
	def maxi(self,array):
		sums=array[0]
		maxs=array[0]
		
		for i in range(len(array)):
			if sums < 0:
				sums=array[i]
			else:
				sums+=array[i]
			maxs=max(sums,maxs)
		return maxs
def main():
	array=list(map(int,input("enter the elements:").split()))
	s=Solution()
	maxi=s.maxi(array)
	print("maximum sub array sum is :",maxi)
	
if __name__=="__main__":
	main()

class Solution():
	def product(self,array):
		output=[1]*len(array)
		left=[1]*len(array)
		right=[1]*len(array)
		
		for i in range(1,len(array)):
			left[i]=left[i-1]*array[i-1]
		for i in range(len(array)-2,-1,-1):
			right[i]=right[i+1]*array[i+1]
		for i in range(len(array)):
			output[i]=left[i]*right[i]
		
		return output

def main():
	array=list(map(int,input("enter the elements :").split()))
	s=Solution()
	product=s.product(array)
	print("the product is :",product)	

if __name__=="__main__":
	main()

class Solution():
	def missing(self,array):
		seen=[0]*(len(array)+1)
		for i in range(len(array)):
			seen[array[i]]=1
		for i in range(len(seen)):
			if seen[i]==0: 
				return i
			
def main():
	array=list(map(int,input("enter the elements in the list:").split()))
	s=Solution()
	missing=s.missing(array)
	print("the missing number is ",missing)
if __name__=="__main__":
	main()

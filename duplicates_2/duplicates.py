class Solution():
	def duplicates(self,k,array):
		dictionary={}
		for i in range(len(array)):
			if array[i] not in dictionary:
				dictionary[array[i]]=i
			elif abs( dictionary[array[i]]-i)<=k:
				return True
			else:
				dictionary[array[i]]=i
		return False

def main():
	array=list(map(int,input("enter the elements in the array:").split()))
	k=int(input("enter k:"))
	print("the array is",array)
	s=Solution()
	duplicate=s.duplicates(k,array)
	print(duplicate)
if __name__== "__main__":
	main()

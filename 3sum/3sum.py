class Solution:
	def triple(self, array):
		array.sort()
		result = []
		for i in range(len(array)):
			if i>0 and array[i]==array[i-1]:
				continue
			left=i+1
			right=len(array)-1
			
			
			
			while left< right:
				total=array[i]+array[left]+array[right]
				if total<0:
					left+=1
				elif total>0:
					right-=1
				else:
					result.append([array[i],array[left],array[right]])
					left+=1
					right-=1
					while left <right and array[left]==array[left-1]:
						left+=1
					while left <right and array[right]==array[right+1]:
						right-=1	
		return result


def main():
	array = list(map(int, input("Enter elements separated by spaces: ").split()))
	s = Solution()
	triplets = s.triple(array)

	print("The triplets are:", triplets)


if __name__ == "__main__":
	main()

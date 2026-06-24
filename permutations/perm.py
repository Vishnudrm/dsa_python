class Solution:
	def permu(self,array):
		result=[]
		if len(array)==0:
			return [[]]
		else:
			perms=self.permu(array[1:])
			for p in perms:
				for i in range(len(p)+1):
					p_copy=p.copy()
					p_copy.insert(i,array[0])
					result.append(p_copy)
		return result
def main():
	array=list(map(int,input("enter the elements:").split()))
	s=Solution()
	perm=s.permu(array)
	print("the permutations are",perm)
if __name__=="__main__":
	main()

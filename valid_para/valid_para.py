class Solution:
	def check(self,para):
		stack=[]
		pairs = {'(': ')', '{': '}', '[': ']'}
		for ch in para:
			if ch in pairs:
				stack.append(ch)
			else:
				if not stack:
					return False
				else:
					j=stack.pop()
					if pairs[j]!=ch:
						return False
		return len(stack)==0


def main():
	para=(input("enter the paranthesis"))
	s=Solution()
	ch=s.check(para)
	if ch:
		print("it is valid")
	else :
		print("it is not valid")

if __name__=="__main__":
	main()

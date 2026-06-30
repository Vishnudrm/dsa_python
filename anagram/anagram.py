class Solution():
	def anagram(self,s,t):
		if len(s)!=len(t):
			return False
		else:
			sd={}
			for ch in s:
				if ch in sd:
					sd[ch]+=1
				else:
					sd[ch]=1
			for ch in t:
				if ch in sd:
					sd[ch]-=1
				else:
					return False
			for ch in sd:
				if sd[ch]!=0:
					return False
			
			return True
def main():
	s=str(input("enter the first string:"))
	t=str(input("enter the second string:"))
	
	so=Solution()
	anagram=so.anagram(s,t)
	print(anagram)
if __name__=="__main__":
	main()

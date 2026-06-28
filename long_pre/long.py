class Solution():
	def lon(self,strs):
		result=""
		
		if not strs:
			return ""
		
		
		else:
			strs.sort()
			first=strs[0]
			second=strs[-1]
			
			l1=min(len(first),len(second))
			
			for i in range(l1):
				if first[i]==second[i]:
					result+=first[i]
				else:
					break
		return result




def main():
	strs=list(map(str,input("enter the strings:").split()))
	s=Solution()
	lon=s.lon(strs)
	print("longest prefix is:",lon)
if __name__=="__main__":
	main()

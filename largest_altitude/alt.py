class Solution():
	def large(self,gain)->int:
		large=0
		curr=0
		for g in gain:
			curr+=g
			large=max(large,curr)
		return large
def main():
	gain = []
	num = int(input("Enter the number of altitudes: "))
	print("Enter the gain values:")
	for i in range(num):
		val = int(input())
		gain.append(val)
	print(gain)
	s=Solution()
	highest=s.large(gain)
	print("highest altitude is ",highest)
if __name__=="__main__":
	main()

class Solution():
	def max_profit(self,prices):
		curr=0
		profit=0
		minimum=prices[0]
		for i in range(1,len(prices)):
			profit=prices[i]-minimum
			minimum=min(minimum,prices[i])
			curr=max(curr,profit)
		return curr
def main():
	prices=list(map(int,input("enter the stock prices: ").split()))
	s=Solution()
	max_profit=s.max_profit(prices)
	print("the maximum profit is ",max_profit)
if __name__=="__main__":
	main()

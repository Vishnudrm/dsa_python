class Solution():
	def maximum(self,coins,costs):
		n=0
		count=[0]*(max(costs)+1)
		for cost in costs:
			count[cost]+=1
		for price in range(1,len(count)):
			if count[price]==0:
				continue
			else:
				afford=coins//price
				bought=min(afford,count[price])
				n+=bought
				coins-=bought*price
		return n

def main():
	costs=list(map(int,input("enter the price of the icecreams").split()))
	coins=int(input("enter the coins"))
	s=Solution()
	max_ice=s.maximum(coins,costs)
	print("maximum number of icecreams :",max_ice)
	
if __name__=="__main__":
	main()
	

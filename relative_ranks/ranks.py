class Solution():
	def rank(self,score):
		dictionary={}
		output=[""]*len(score)
		for i in range(len(score)):
			dictionary[score[i]]=i
		score.sort(reverse=True)
		for i in range(len(score)):
			if i==0:
				output[dictionary[score[i]]]="Gold Medal"
			elif i==1:
				output[dictionary[score[i]]]="Silver Medal"
			elif i==2:
				output[dictionary[score[i]]]="Bronze Medal"
			else:
				output[dictionary[score[i]]]=str(i+1)
		return output
def main():
	score=list(map(int,input("enter the score:").split()))
	s=Solution()
	ranks=s.rank(score)
	print("ranks are :",ranks)

if __name__=="__main__":
	main()

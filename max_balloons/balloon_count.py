class Solution:
    def maxBalloons(self,text):
        n=[]
        alph={"a":0,"b":1,"l":2,"n":3,"o":4}
        need_count=[1,1,2,1,2]
        count=[0]*5
        for ch in text:
            if ch in alph:
                count[alph[ch]]+=1
        for i in range(0,5):
            n.append(count[i]//need_count[i])
        return min(n)
def main():
    text=str(input("Enter the text: "))
    print(text)
    s=Solution()
    balloon_count=s.maxBalloons(text)
    print("maximum number of balloons :",balloon_count)

if __name__ == "__main__":
    main()
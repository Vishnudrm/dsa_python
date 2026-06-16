class solution:
    def rev_int(self,x:int)->int:
        int_max=2**31 -1
        sign = -1 if x<0 else 1
        x=abs(x)
        result=0
        while x!=0:
            digit=x%10
            x=x//10
            result=result*10+digit
        if result>int_max:
            return 0
        return sign*result
            

def main():
    num=int(input("enter the integer:"))
    sol=solution()
    rev=sol.rev_int(num)
    print("the reverse of the integer is:",rev)    
if __name__=="__main__":
    main()

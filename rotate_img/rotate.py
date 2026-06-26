class Solution():
	def img(self,matrix):
		for i in range(len(matrix)-1):
			for j in range(i+1,len(matrix)):
				matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
		for row in matrix:
			row.reverse()
		
		return matrix



def main():
	n=int(input("enter the size of the matrix:"))
	matrix=[]
	for i in range(n):
		row=list(map(int,input("enter the elements:").split()))
		matrix.append(row)
	s=Solution()
	img=s.img(matrix)
	print("the image is :",img)



if __name__=="__main__":
	main()

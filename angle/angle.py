class Solution():
	def angle(self,hour,minutes):
		min_angle=minutes*6
		hour_angle=hour*30+0.5*minutes
		angle=abs(hour_angle-min_angle)
		return min(angle,360-angle)
def main():
	hour,minutes=map(int,input("enter the hour and minutes").split())
	print("hour and minutes are:",hour,minutes)
	s=Solution()
	angle=s.angle(hour,minutes)
	print("the angle is",angle)	
if __name__=="__main__":
	main()

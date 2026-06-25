class Solution():
    def missing(self, array, duration):
        time = 0
        poison = 0
        curr = 0
        for i in range(len(array)):
            if poison <= array[i]:
                poison = array[i] + duration
                time += duration
            else:
                curr = duration - (poison - array[i])
                poison = array[i] + duration
                time = time + curr
        return time

def main():
    array = list(map(int, input("enter the elements in the list: ").split()))
    duration = int(input("enter the duration: "))
    s = Solution()
    time = s.missing(array, duration)
    print("the missing number is ", time)

if __name__ == "__main__":
    main()
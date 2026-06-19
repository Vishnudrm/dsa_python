class Solution:
    def plus(self, numb):
        num = 0

        for d in numb:
            num = num * 10 + d

        num += 1

        return [int(x) for x in str(num)]


def main():
    num = int(input("Enter the number: "))

    numb = [int(x) for x in str(num)]

    print("Digits:", numb)

    s = Solution()

    plus_one = s.plus(numb)

    print("After adding one:", plus_one)


if __name__ == "__main__":
    main()

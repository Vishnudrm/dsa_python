class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            v1 = int(a[i]) if i >= 0 else 0
            v2 = int(b[j]) if j >= 0 else 0

            total = v1 + v2 + carry
            carry = total // 2
            result.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(reversed(result))


def main():
   
    a = input("Enter first binary string (a): ").strip()
    b = input("Enter second binary string (b): ").strip()

    sol = Solution()

    result = sol.addBinary(a, b)

    print(f"Sum of {a} and {b} in binary is: {result}")


if __name__ == "__main__":
    main()

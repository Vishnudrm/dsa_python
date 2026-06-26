class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) :
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)
def main():
    array = list(map(int, input("Enter the sorted elements: ").split()))
    array.sort()
    s = Solution()
    root = s.sortedArrayToBST(array)
    print("Preorder Traversal of BST:")
    preorder(root)
if __name__ == "__main__":
    main()

# Convert Sorted Array to Binary Search Tree

## Problem Statement

Given a sorted array of integers in ascending order, construct a **height-balanced Binary Search Tree (BST)**.

A height-balanced BST is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

The objective is to convert the sorted array into a BST while maintaining the height-balanced property, ensuring efficient search, insertion, and deletion operations.

### Example

**Input**

```text
nums = [-10, -3, 0, 5, 9]
```

**Output (One Possible BST)**

```text
        0
      /   \
    -10    5
      \      \
      -3      9
```

Another valid height-balanced BST may also be returned.

---

# Approach

## Intuition

Since the array is already sorted, the middle element naturally divides the array into two equal halves.

* Elements to the left of the middle are smaller.
* Elements to the right of the middle are larger.

Therefore, choosing the middle element as the root automatically satisfies the Binary Search Tree property. Repeating this process recursively for both halves results in a balanced tree.

---

## Algorithm

1. **Base Case**

   * If the array is empty, return `None`.
   * This indicates that there are no nodes to construct.

2. **Find the Middle Element**

   * Compute the middle index:

   ```python
   mid = len(nums) // 2
   ```

   * The middle element becomes the root of the current subtree.

3. **Create the Root Node**

   ```python
   root = TreeNode(nums[mid])
   ```

4. **Construct the Left Subtree**

   * Recursively build the BST using all elements before the middle.

   ```python
   root.left = sortedArrayToBST(nums[:mid])
   ```

5. **Construct the Right Subtree**

   * Recursively build the BST using all elements after the middle.

   ```python
   root.right = sortedArrayToBST(nums[mid + 1:])
   ```

6. **Return the Root**

   * Once both subtrees are created, return the current root.

---

## Working Example

### Input

```text
[1, 2, 3, 4, 5, 6, 7]
```

### Step 1

Middle element:

```text
4
```

Tree:

```text
    4
```

---

### Step 2

Left half:

```text
[1, 2, 3]
```

Middle:

```text
2
```

Right half:

```text
[5, 6, 7]
```

Middle:

```text
6
```

Tree becomes:

```text
        4
      /   \
     2     6
```

---

### Step 3

Process the remaining halves.

Left subtree:

```text
[1]
[3]
```

Right subtree:

```text
[5]
[7]
```

Final BST:

```text
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```

The tree is height-balanced, and every node satisfies the Binary Search Tree property.

---

# Why This Approach Works

At every recursive call:

* The middle element is selected as the root.
* All elements in the left subarray are smaller than the root.
* All elements in the right subarray are larger than the root.

Thus, the BST property is preserved.

Additionally, selecting the middle element minimizes the height of the tree, producing a balanced BST.

---

# Time Complexity

### Tree Construction

Each element is used exactly once to create a tree node.

* Creating each node takes **O(1)** time.
* There are **n** nodes.

However, this implementation uses Python list slicing:

```python
nums[:mid]
nums[mid + 1:]
```

Each slicing operation creates a new list, which requires copying elements.

Therefore, the overall time complexity is:

**O(n log n)**

### Optimized Version

If instead of slicing, indices (`left` and `right`) are passed recursively, no extra copying occurs.

Time Complexity:

```text
O(n)
```

---

# Space Complexity

### Recursive Stack

The recursion depth is equal to the height of the balanced BST.

```text
O(log n)
```

### Additional Space Due to Slicing

Since new subarrays are created during recursion, additional memory is required.

Overall auxiliary space:

```text
O(n)
```

### Optimized Version

Without slicing (using indices), only the recursion stack remains.

Space Complexity:

```text
O(log n)
```

---

# Summary

* Choose the middle element as the root.
* Recursively construct the left subtree from the left half.
* Recursively construct the right subtree from the right half.
* The approach guarantees a height-balanced Binary Search Tree.
* Current implementation:

  * **Time Complexity:** `O(n log n)` (due to list slicing)
  * **Space Complexity:** `O(n)` (due to slicing)
* Optimized implementation (using indices):

  * **Time Complexity:** `O(n)`
  * **Space Complexity:** `O(log n)`

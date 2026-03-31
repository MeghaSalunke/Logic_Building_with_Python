'''
Q. Given an array of integers, find and return the smallest
element present in the array.
Example 1:
Input: nums = [5, 8, 1, 4, 7]
Output: 1
Explanation: Among all the elements, 1 is the minimum value.
Example 2:
Input: nums = [3,2,4]
Output: 2
Example 3:
Input: nums = [3,3]
Output: 3
'''

def find_min():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    return min(nums)

print(find_min())
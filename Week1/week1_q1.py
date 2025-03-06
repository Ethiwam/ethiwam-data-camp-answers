"""
File Name: week1_q1.py
Coder: Ethan Iwama
Purpose: Solution to Week 1 Problem 1
"""

nums = [0, 1]

for _ in range(8):  # Range is (wanted range) - 2
    index = len(nums)
    new_val = nums[index-1] + nums[index-2]
    nums.append(new_val)

print(nums)
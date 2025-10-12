from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    max_streak = 0
    current = 0
    for x in nums:
        if x > 0:
            current += 1
            if current > max_streak:
                max_streak = current
        else:
            current = 0
    return max_streak

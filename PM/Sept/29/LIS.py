def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = length_of_lis(nums)
print(result)  # Output: 4 (The longest increasing subsequence is [2, 3, 7, 101])

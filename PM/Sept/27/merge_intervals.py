'''
Write a Python function called merge_intervals that takes a list of intervals as input,
where each interval is represented as a pair of integers [start, end]. 
Your function should merge overlapping intervals and return a list of non-overlapping intervals in ascending order.

'''
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        previous_interval = merged_intervals[-1]

        if current_interval[0] <= previous_interval[1]:
            previous_interval[1] = max(previous_interval[1], current_interval[1])
        else:
            merged_intervals.append(current_interval)

    return merged_intervals

intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals1))  # [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1, 4], [4, 5]]
print(merge_intervals(intervals2))  # [[1, 5]]

intervals3 = [[1, 4], [0, 4]]
print(merge_intervals(intervals3))  # [[0, 4]]

'''
Time Complexity: O(NlogN)
Space Complexity: O(N)
'''

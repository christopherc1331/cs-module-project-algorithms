'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from ring_buffer import RingBuffer


from collections import deque


def sliding_window_max(nums, k):
    # Your code here

    output = []

    p = k
    for i in range(len(nums)):
        if p <= len(nums):
            sliced_nums = nums[i:p]

            p += 1
            max = None
            for num in sliced_nums:
                if max is None:
                    max = num
                else:
                    if num > max:
                        max = num

            output.append(max)
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

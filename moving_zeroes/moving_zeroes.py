'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

# loop through arr
# pop if zero
# append popped value to end of arr
# return mutated arr
    i = 0
    k = len(arr) - 1
    for i in range(0, k ):
        while arr[i] == 0 and i < k:
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1



    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
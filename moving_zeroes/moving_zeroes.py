'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # you can make a list for all 0s and then concat
    # but the challenge is to do an in place solution
    # usually when you use an in place you need to use pointers

    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            # swap, increment L, decrement R
            arr[left], arr[right] = arr[right], arr[left] 
            left += 1 
            right += -1
        else:
            if arr[left] != 0:
                # increment left
                left += 1
            if arr[right] == 0:
                # decrement right
                right += -1
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
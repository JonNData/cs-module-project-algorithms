'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Create a list, add nums to it, if repeated, remove, return list value at end
    # no_dups = []
    # for num in arr:  O(n^2)
    #     if num not in no_dups:
    #         no_dups.append(num)
    #     else:
    #         no_dups.remove(num)
    # return no_dups[0]

    # Now optimize
    # dict would be faster to lookup

    counts = {}
    for num in arr: # O(n)
        # get words into dict with count 1
        if num not in counts: # O(n)
            counts[num] = 1
        # repeats add to the count 
        else:
            counts[num] += 1
    for key, value in counts.items(): # O(n)
        if value == 1:
            return key



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
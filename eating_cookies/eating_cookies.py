'''
Input: an integer
Returns: an integer
'''
from itertools import combinations
def eating_cookies(n):
    # Your code here
    # brute force would be to use combinations
    # use a counter ? I think recursive would be good here
    # cookie breakdown:
        # all ones
        # if > 2
            # one 2, rest 1s
            #  if >3 , two 2s, rest 1s
        # This does not look good, lets just do combinations
    full_comb = combinations([1,2,3], n)
    correct_sum = [x for x in full_comb if sum(x)==n]
    return len(correct_sum)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

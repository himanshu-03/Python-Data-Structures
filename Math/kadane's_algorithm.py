def max_subarray_sum(nums):
    # Initialize variables to keep track of the maximum subarray sum
    
    max_ending_here = nums[0]  # Maximum sum ending at the current position
    max_so_far = nums[0]  # Maximum sum seen so far

    # Iterate through the array, starting from the second element
    for i in range(1, len(nums)):
        # Calculate the maximum sum ending at the current position by considering whether it's better to 
        # start a new subarray or extend the previous one.
        max_ending_here = max(nums[i], max_ending_here + nums[i])

        # Update the maximum sum seen so far by comparing it with the   maximum sum ending at the current position.
        max_so_far = max(max_so_far, max_ending_here)

    # The 'max_so_far' variable now contains the maximum subarray sum.
    return max_so_far
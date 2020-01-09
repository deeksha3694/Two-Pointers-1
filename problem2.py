def tripletZero(nums):
    found = False
    n = len(nums)
    nums.sort()
    for i in range(0, n-1):
        low = i + 1
        high = n-1
        current = nums[i]
        while(low < high):
            if (current + nums[low] + nums[high]) == 0:
                print(current, nums[low], nums[high])
                low += 1
                high -= 1
                found = True
            elif (current + nums[low] + nums[high]) < 0:
                low += 1
            else:
                high -= 1
    
    if(found == False):
        return 0

nums = [-1, 0, 1, 2, -1, -4]
print(tripletZero(nums))
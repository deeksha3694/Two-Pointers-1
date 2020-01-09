def container(nums):
    l = 0
    r = len(nums) - 1
    area = 0

    while l < r:
        area = max(area, (min(nums[l], nums[r])* (r-l)))
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return area

nums = [1,8,6,2,5,4,8,3,7]
print(container(nums))
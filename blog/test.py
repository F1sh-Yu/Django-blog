def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    def search(nums, left, right, target):
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] > target:
            search(nums, left, mid - 1, target)
        elif nums[mid] < target:
            search(nums, mid + 1, right, target)
        else:
            return mid

    return search(nums, left, right, target)

print(searchInsert([1,3,5,6], 5))
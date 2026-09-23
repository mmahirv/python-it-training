def apply(operation, *nums, **infos):
    if operation == 'adding':
        return_value = sum(nums)
    elif operation == 'substraction':
        return_value = nums[0] - sum(nums[1:])
    elif operation == 'multply':
        return_value = 1
        for n in nums:
            return_value *= n
    elif operation == 'division':
        return_value = nums[0]
        for n in nums[1:]:
            return_value /= n
    elif operation == 'print':
        return_value = []
        for key, value in infos.items():
            return_value.append(f"{key}: {value}")
        return_value = '; '.join(return_value)
    return return_value


print(apply('adding', 1, 2, 3, 4))
print(apply('substraction', 10, 2, 3))
print(apply('multply', 2, 3, 4))
print(apply('division', 100, 2, 5))
print(apply('print', name='Ada', age=36))
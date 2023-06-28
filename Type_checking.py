def mean(*args):
    nums = []
    for i in args:
        if type(i) is int or type(i) is float:
            nums.append(i)
    if len(nums) == 0:
        return 0.0
    else:
        return sum(nums) / len(nums)

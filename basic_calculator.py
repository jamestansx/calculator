def add(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum


def sub(nums):
    sub = 0
    for i in range(len(nums)):
        sub -= nums[i]
    return sub


def mul(nums):
    mul = nums[0]
    for i in range(len(nums)):
        mul *= nums[i]
    return mul


def div(nums):
    div = nums[0]
    for i in range(len(nums)):
        div /= nums[i]
    return div


nums = [int(x) for x in input("Enter the numbers: ").split()]
arithmetic = input("Which arithmetic operator to use: ")

arithmetic_operator = {"+": add(nums), "-": sub(nums), "*": mul(nums), "/": div(nums)}


print(arithmetic_operator[arithmetic])

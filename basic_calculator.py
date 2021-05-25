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
    for i in range(1, len(nums)): # fixed issue where it would multiply the 1st number twice
        mul *= nums[i]
    return mul

def div(nums):
    div = nums[0]
    for i in range(1, len(nums)): # fixed issue where it would divide the 1st number twice
        div /= nums[i]
    return div

<<<<<<< HEAD

if __name__ == '__main__':
    nums = [int(x) for x in input("Enter the numbers: ").split()]  # can recieve indefinite inputs
    arithmetic = input("Which arithmetic operator to use: ")  # +,-,*,/
=======
nums = [int(x) for x in input("Enter the numbers: ").split()]  # can recieve indefinite inputs
# converted arithmetic to a tuple
arithmetic = (str(input("Which arithmetic operator to use: "))).split()  # +,-,*,/
>>>>>>> fixed multi-operator and mult and div errors

    arithmetic_operator = {"+": add(nums), "-": sub(nums), "*": mul(nums), "/": div(nums)}

<<<<<<< HEAD

    print(arithmetic_operator[arithmetic])
=======
# initialized a for loop for printing the values
for x in range(len(arithmetic)):
    str = arithmetic[x]
    print(arithmetic_operator[str])
>>>>>>> fixed multi-operator and mult and div errors

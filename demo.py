def first_last6(nums):
    if (nums[0] == 6) or (nums[len(nums)-1] == 6):
        return True
    else:
         return False
a=first_last6([1,2,6])
print(a)
b=first_last6([6,1,2,3])
print(b)
c=first_last6([13,6,1,2,3])
print(c)
print("==========================================================")
def same_first_last(nums):
    if len(nums)>0:
        if nums[0] == nums[len(nums) - 1]:
            return True
        else:
            return False
    else:return False
a=same_first_last([1,2,3])
print(a)
b=same_first_last([1,2,3,1])
print(b)
c=same_first_last([1,2,1])
print(c)
print("==========================================================")
def common_end(a, b):
    if (a[0] == b[0]) or (a[len(a)-1] == b[len(b)-1]):
        return True
    else:
        return False
a=common_end([1,2,3],[7,3])
print(a)
b=common_end([1,2,3],[7,3,2])
print(b)
c=common_end([1,2,3],[1,3])
print(c)
print("==========================================================")
def sum3(nums):
    return nums[0]+nums[1]+nums[2]
a=sum3([1,2,3])
print(a)
b=sum3([5,11,2])
print(b)
c=sum3([7,0,0])
print(c)
print("==========================================================")
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
a=rotate_left3([1,2,3])
print(a)
b=rotate_left3([5,11,9])
print(b)
c=rotate_left3([7,0,0])
print(c)
print("==========================================================")
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]
a=reverse3([1,2,3])
print(a)
b=reverse3([5,11,9])
print(b)
c=reverse3([7,0,0])
print(c)
print("==========================================================")
def max_end3(nums):
    if nums[0]>nums[2]:
        return [nums[0],nums[0],nums[0]]
    else:
        return [nums[2],nums[2],nums[2]]
a=max_end3([1,2,3])
print(a)
b=max_end3([11,5,9])
print(b)
c=max_end3([2,11,3])
print(c)
print("==========================================================")
def sum2(nums):
    if len(nums) == 0:return 0
    elif len(nums) == 1:
        return nums[0]
    else:return nums[0] + nums[1]
a=sum2([1,2,3])
print(a)
b=sum2([1,1])
print(b)
c=sum2([1,1,1,1])
print(c)
print("==========================================================")
def middle_way(a, b):
    return [a[1],b[1]]
a=middle_way([1,2,3],[4,5,6])
print(a)
b=middle_way([7,7,7],[3,8,0])
print(b)
c=middle_way([5,2,9],[1,4,5])
print(c)
print("==========================================================")
def make_ends(nums):
    return [nums[0], nums[-1]]
a=make_ends([1,2,3])
print(a)
b=make_ends([1,2,3,4])
print(b)
c=make_ends([7,4,6,2])
print(c)
print("==========================================================")
def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
         return False
a=has23([2,5])
print(a)
b=has23([4,3])
print(b)
c=has23([4,5])
print(c)

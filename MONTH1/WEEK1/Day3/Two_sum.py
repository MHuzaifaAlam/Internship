#leet code probelm 
def two_sum(nums,target):
    seen={}
    print("the target is ",target)
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return[seen[complement],i]
        seen[num]=i
    return None

print("the indexes are",two_sum([1,2,3,4,5,6],11))



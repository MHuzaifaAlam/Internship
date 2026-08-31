# Searching & counting
# Find the maximum and minimum in a list without using max()/min()
# Count how many times a given element appears in a list
# Check if a given element exists in a list without using in
# Find the index of the first occurrence of an element without using .index()
# Count even and odd numbers in a list
# Count positive, negative, and zero values in a list

new_list=[1,2,3,4,1,5,6,7,8,9]
max_val=new_list[0]
for num in new_list:
     if num > max_val:
        max_val=num

print(max_val)

min_val=new_list[0]
for num in new_list:
     if num < min_val:
        min_val=num

print(min_val)


target=int(input("Enter the num to check : "))
count=0
for num in new_list:
    if target==num:
        count+=1
print(count)

given_num=int(input("Enter the element: "))
found=False
for num in new_list:
    if given_num==num:
        found=True
        break
if found:
    print(f"Number Found {given_num}")
else:
    print("Number not found")


target2=int(input("Enter the number to find"))
index=0
found_index=-1
for num1 in new_list:
    if num1 == target2:
        found_index=index
        break
    index+=1

print(found_index)


even_count=0
odd_count=0

for num3 in new_list:
    if num3%2==0:
        even_count+=1
        print(f"Even Number{num3}")
    else:
        odd_count+=1
        print(f"ODD Number{num3}")

print("EVEN NUM :",even_count)
print("ODD NUM :",odd_count)

List_new=[-2,1,-2,3,4,5,-6,0,2,0,1,-2]
p_list=[]
negtive_list=[]
count_postive=0
count_negative=0
count_zero=0
for i in List_new:
    if i >0:
        p_list.append(i)
        count_postive+=1
    elif i <0:
        negtive_list.append(i)
        count_negative+=1
    elif i ==0:
        count_zero+=1
print(f"The positive Numbers are : {count_postive}   {p_list} ")
print(f"The Negative Numbers are : {count_negative}  {negtive_list} ")
print(f"The Zero values are : {count_zero}")




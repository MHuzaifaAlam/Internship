# Basics — creating & accessing
# Create a list of first 10 natural numbers using a loop (not range() shortcuts)
# Access and print the first, last, and middle element of a list
# Print a list in reverse order without using reverse() or slicing
# Find the length of a list without using len()
# Take N inputs from the user and store them in a list
num_list=[]
i=0
while i <10:
    input_num=input(f"Enter the num of index {i} :")
    num_list.append(input_num)
    i+=1

print(num_list)

print(num_list[0])
print(num_list[5])
print(num_list[-1])

rev_list=[]
i=len(num_list)-1
while i >=0:
    rev_list.append(num_list[i])
    i-=1 

print(rev_list)

count=0
while count<len(num_list):
    count+=1
print(f"Count:{count}")

new_list=[]
num=int(input("Enter the num :"))
i=0
while i <num:
    new_num=input("Enter List value :")
    new_list.append(new_num)
    i+=1

print(new_list)


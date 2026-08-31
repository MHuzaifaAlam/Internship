# strings excersices 
#reverseing a string
my_str="My name is Huzaifa"
reverse=my_str[::-1]
print(reverse)

# palindrome + F string
palindrome="AOA"
palindrome_reverse=palindrome[::-1]
if palindrome == palindrome_reverse:
    print(f"The string {palindrome} is palindrome")
else:
    print("The String is not a palindrome")
#Slicing 
my_str="hello world"
print(my_str[1:4])

# strings operation
my_str="hello world"
num_find=my_str.find('r')
print(num_find)

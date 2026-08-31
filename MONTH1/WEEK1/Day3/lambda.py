# lambda function using filter
numbers=[1,3,4,2,4,5,6]
even=list(filter(lambda x:x%2==0,numbers))
print("the even sorted list with lamba function is")
print(even)

# problem  Sort the list of the cities with length of the word and store it into a list 
name_cities=["Jaipur","lahore","Faislabad","karachi","Amritsar"]
sorted_cities=list(sorted(name_cities,key=lambda x :len(x)))
print(sorted_cities)

#lamba function using Map function 
numbers=[1,3,4,6,8,9]
square=list(map(lambda x:x**2,numbers))
print(square)
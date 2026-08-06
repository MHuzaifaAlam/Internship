#create Tuple 
user_info=("HUZAIFA",34,"Python Developer")
print(user_info[0])

#create tuple by using tuple()
developer="Huzaifa"
print(tuple(developer))

#unpack the tuple items
user_info=("HUZAIFA",34,"Python Developer")
name,age,role=user_info
print(name)
print(age)
print(role)

user_info=("HUZAIFA",34,"Python Developer",34,"ALi",34)
user_info.index(34,3)
# it sorts based on the length as the length pass as key 
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))
#sorted functions on tuples using reverse
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True))


pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
person={
    'name':'Huzaifa',
    'age': 39,
    'Gender':'Male'
}
print(person.get('age'))
print(pizza)

# excersices 
#word frequency counter
from collections import Counter
a="The cat sat on the mat the cat run the cat was sad"
b=Counter(a.split())
dict(b)
print(b)



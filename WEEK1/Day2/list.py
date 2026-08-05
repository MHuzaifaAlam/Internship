#append method
fruits=["apple","banana","strawbery","bluberry"]
fruits.append("grapes")
print(fruits)

#extends method
clothes=["shirts","pants","sweater","shoes"]
winter_clothes=["Jorts","Hoodie","Sweater","Socks"]
clothes.extend(winter_clothes)
print(clothes)

#remove the element from the list POP()
fruits=["apple","banana","strawbery","bluberry"]
fruits.pop()
print(fruits)
# if we want to remove from the prticular index 
fruits=["apple","banana","strawbery","bluberry"]
fruits.pop(2)
print(fruits)
# del method
fruits=["apple","banana","strawbery","bluberry"]
del fruits[1]
print(fruits)
#remove method
fruits=["apple","banana","strawbery","bluberry"]
fruits.remove("bluberry")
print(fruits)
#clear method
fruits=["apple","banana","strawbery","bluberry"]
fruits.clear()
print(fruits)
#sort  method
#remove method
fruits=["apple","strawbery","bluberry","banana"]
fruits.remove("bluberry")
print(fruits)
# sort and sorted method
fruits=["apple","strawbery","bluberry","banana"]
fruits.sort()
print(fruits)

#using sorted function
fruits=["apple","strawbery","bluberry","banana"]
new_sorted=sorted(fruits)
print(fruits)
print(new_sorted)

#count mehthod()
fruits=["apple","banana","strawbery","bluberry","banana"]
item_occurence=fruits.count("banana")
print(item_occurence)

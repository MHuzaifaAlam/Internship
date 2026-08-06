#example of for loop
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for catagorey in categories:
    for food in foods:
        print(categories,food)

#example of While loop
secret_Number=3
guess=0
while guess!=secret_Number:
    guess=int(input("Guess the Number again "))
    if guess!=secret_Number:
        print('Wrong Try Again')

print(f'you Got it {guess} is Correct')

# vowles finding excersice 
words=["sky","person","hello","love","fox"]
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"the word {word} Has vowel {letter}")
            break
        else:
            print(f"the {word} Word has no vowel")


#range function practice
for num in range(2, 11, 2):
    print(num)
#reverse range pracitce
for num in range(40, 0, -5):
    print(num)

#even num 
even_num=[]
for num in range(1,21):
    if num%2==0:
        even_num.append(num)

print(even_num)
#comprehensive list 
even_number=[num for num in range(21) if num %2 == 0]
print(even_num)
class Cat:
    def speak(self):
        return "A cat Says Meoww"
class Bird:
    def speak(self):
        return "A bird tweet"
class Monkey:
    def speak(self):
        return "A Monkey do ooohh haaaahaaaa ooooohoooo haaaahaaaa"



def animal_sound(animal):
    print(animal.speak)



animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())
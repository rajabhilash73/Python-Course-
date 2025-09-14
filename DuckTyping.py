"""
Duck Typing = A concept where the class of an object is less important that the methods/attributes.
Class type is not checked if minimum methods/attributes are present.
"If it is walk like a duck, and quacks like a duck, then it must be a duck."
"""
class Duck:
    def walk(self):
        print("The duck is walking.")

    def talk(self):
        print("The duck is quacking.")

class Chicken:
    def walk(self):
        print("The chicken is walking.")

    def talk(self):
        print("The chicken is clucking.")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the quitter.")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

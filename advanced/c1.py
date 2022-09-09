class Dog:

    #attributes
    age = 0
    weight = 0
    height = 0
    color = ""
    breed = ""
    gender = ""

    #methods
    def bark(self):
        print("bow" * 3)

    def wag(self):
        print('Wags Tails')
    
    def eat(self, food):
        print(f'dog {food} kha skta hai')

tommy = Dog()     #calling the constructor
tommy.age = 3
tommy.breed = "street Dog"
tommy.color = 'black'
tommy.gender = 'male'
tommy.height = 1
tommy.weight = 5

kallu = Dog()
kallu.age = 5
kallu.breed = "husky"
kallu.color = 'black n white'
kallu.gender = 'male'
kallu.height = 0.8
kallu.weight = 6

charlie = Dog()
charlie.age = 4
charlie.breed = "bull Dog"
charlie.color = 'grey'
charlie.gender = 'female'
charlie.height = 1.1
charlie.weight = 8


kallu.bark()
kallu.eat('fish')
charlie.eat('dog-fish')
tommy.eat('bachi hui rooti')
tommy.eat('bachi hui daal')
tommy.bark()
kallu.bark()



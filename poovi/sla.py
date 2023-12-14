class animal:
    def __init__(self, color):
        self.color = color
    def walk(self):
        print('bora passear')
    def bite(self):
        print('se me atacar, vou te atacar')

class dog(animal):
    def __init__(self, color):
        super().__init__(color)
    def bark(self):
        print('au aua au')
    def drool(self):
        print('shclop!')

class Gato(animal):
    def __init__(self, color):
        super().__init__(color)
    def meow(self):
        print('Miau')
    def purr(self):
        print('Prrrrrrruuuu')

class peixe(animal):
    def __init__(self, color):
        super().__init__(color)
    def nadar(self):
        print('nadar')


a = peixe('caramelo')
a.bite()
a.walk()
a.drool()



# class Cao:
#     def __init__(self, color):
#         self.color = color
#     def walk(self):
#         print(' T passeando')
#     def bite(self):
#         print('Ovo mord\ˆe')
#     def bark(self):
#         print('au au auuuu au')
#     def drool(self):
#         print('slop! blob! blab!')

# # class Gato(Dog):
# #     def __init__(self, color):
# #         super().__init__(color)
# #     def meow(self):
# #         print('Miau')
# #     def purr(self):
# #         print('Prrrrrrruuuu')



# class Gato:
#     def __init__(self, color):
#         self.cao = Cao(color)
#         self.color = color
#     def meow(self):
#         print('Miau')
#     def purr(self):
#         print('Prrrrrrruuuu')
#     def walk(self):
#         self.cao.walk()
#     def bite(self):
#         self.cao.bite()

# garfield = Gato('siames')
# garfield.walk()
# garfield.meow()
# garfield.bark() # latir
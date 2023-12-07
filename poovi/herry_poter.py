class bruxo:
    def __init__(self, nome, casa):
        self.nome = nome
        self.casa = casa

# harry = bruxo('harry poter', 'grifinolia')
# draco = bruxo('draco malfoy', 'sonserina')

# print(harry.nome)
# print(harry.casa)
# print(draco.nome)
# print(draco.casa)

# harry.nome = 'vanessa'

# print(harry.nome)
# print(harry.casa)
# print(draco.nome)
# print(draco.casa)

class student:
    def __init__(self, name, mat, n1, n2):
        self.name = name
        self.mat = mat
        self.n1 = n1
        self.n2 = n2

    def cal_media(self):
        return ((2 * self.n1) + (3 * self.n2)) / 5
    
    def is_aprovado(self):
        return self.cal_media() >= 6
    
    def __str__(self):
        return f'''sou {self.name} tirei na N1 {self.n1} e na N2 {self.n2} e fui aprovado? {self.is_aprovado()}'''
    
saulo = student('saulo', '2020', 5, 6.5)

print(saulo)
# print(saulo.cal_media())
# print(saulo.is_aprovado())
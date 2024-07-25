class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        file = open(self.__file_name, 'a')
        current_products = self.get_products()
        for i in products:
            if i.name in current_products:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file.write(str(i) + '\n')
                current_products += str(i) + '\n'
        file.close()


class Product:
    def __init__(self, name, weight, category):
        self.category = category
        self.weight = weight
        self.name = name

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

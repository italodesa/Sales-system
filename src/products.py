class Product:
    def __init__(self,name,price,quantity):
        self.id = None
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod
    def create_product(cls):
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        quantity = int(input("Digite a quantidade do produto: "))
        return cls(name,price,quantity)
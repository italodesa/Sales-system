from files import generate_id
class Product:
    def __init__(self,name,price,quantity,status,product_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
    
    @classmethod
    def create_product(cls):
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        quantity = int(input("Digite a quantidade do produto: "))
        product_id = generate_id('products.json','product_id')
        return cls(name,price,quantity,product_id)
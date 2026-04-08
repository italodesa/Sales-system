from files import generate_id,return_data
class Product:
    def __init__(self,name,price,quantity,product_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = "active"
    
    @classmethod
    def create_product(cls):
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        quantity = int(input("Digite a quantidade do produto: "))
        product_id = generate_id('products.json','product_id')
        return cls(name,price,quantity,product_id)
    
    @staticmethod
    def show_products(cls):
        products = return_data('products.json')

        print("-" * 40)
        print(f"{'ID':<10} {'NOME':<20}")
        print("-" * 40)

        for product in products:
            print(f"{product['product_id']:<10} {product['name']:<20}")

        print("-" * 40)
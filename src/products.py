from files import generate_id,return_data
class Product:
    def __init__(self,name,price,quantity,product_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = "active"

    def remove_stock(self,quantity):
        if quantity <= 0:
            print("Quantidade invalida")
            return False
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True

    @classmethod
    def create_product(cls):
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        quantity = int(input("Digite a quantidade do produto: "))
        product_id = generate_id('products.json','product_id')
        return cls(name,price,quantity,product_id)
    
    @staticmethod
    def show_products():
        products = return_data('products.json')

        print("-" * 60)
        print(f"{'ID':<10} {'NOME':<20} {'QUANTIDADE':<15}")
        print("-" * 60)

        for product in products:
            print(f"{product['product_id']:<10} {product['name']:<20} {product['quantity']:<15}")

        print("-" * 60)

    @classmethod
    def return_product_obj(cls,product_name,product_id):
        products = return_data('products.json')
        if products:
            for product in products:
                if product["name"] == product_name or product["product_id"] == product_id:
                    if product["status"] != "active":
                        print("produto fora de estoque")
                        return None
                    return cls(
                        product["name"],
                        product["price"],
                        product["quantity"],
                        product["product_id"],
                    )
        else:
            print("Nenhum produto cadastrado")
            return None


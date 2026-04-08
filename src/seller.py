from datetime import datetime
from sales import Sale
from products import Product

class Seller:
    def __init__(self,name,password,seller_id=None):
        self.name = name
        self.password = password
        self.seller_id = seller_id
        self.profile = "seller"

    def create_sale(self):
        total = 0.0
        products = []
        while True:
            now = datetime.now()
            print("-" * 50)
            print(" " * 20 + "painel de venda" + " " * 20)
            print("-" * 50)
            print(f"Vendedor: {self.name}")
            print(f"Data: {now.strftime('%d/%m/%Y')}")
            print("[1] Adicionar Produto\n[2] Finalizar compra\n[3] Sair")

            try:
                option = int(input("> "))
            except ValueError:
                print("Digite uma entrada valida")
            
            match option:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    break
            
from datetime import datetime
from sales import Sale
from products import Product
from files import return_data,generate_id,append_file

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
            print(" " * 20 + "Venda" + " " * 20)
            print("-" * 50)
            print(f"Vendedor: {self.name}")
            print(f"Data: {now.strftime('%d/%m/%Y')}")
            print("\n")
            for product in products:
                print(
                    f"Produto: {product.get('name')} | "
                    f"Quantidade: {product.get('quantity')} | "
                    f"Preço: R$ {product.get('quantity') * product.get('price'):.2f}"
                )
            print(f"Total a pagar: {total}")
            print("\n")
            print("[1] Adicionar Produto\n[2] Finalizar compra\n[3] Sair")

            try:
                option = int(input("> "))
            except ValueError:
                print("Digite uma entrada valida")
                continue
            
            match option:
                case 1:
                    Product.show_products()
                    try:
                        id = int(input("Digite o id do produto: "))
                        name = input("Digite o nome do produto: ")
                        quantity = int(input("Digite a quantidade: "))
                    except ValueError:
                        print("Digite valores validos")
                        continue
                    p = Product.return_product_obj(name,id)
                    if p:
                        if p.quantity < quantity:
                            print("Quantidade insuficiente")
                            continue

                        products.append(
                            {
                                "id": p.product_id,
                                "name": p.name,
                                "quantity": quantity,
                                "price": p.price
                            }
                        )
                        total += quantity * p.price
                    else:
                        print("Esse produto não existe")
                        continue
                case 2:
                    if not products:
                        print("Não foi possivel executar a venda")
                        continue
                    c = input("Tem certeza que deseja confirmar a compra? (s/n): ").lower()
                    if c == 's':
                        sale_id = generate_id('sales.json','sale_id')
                        seller_id = self.seller_id
                        seller_name = self.name
                        total_sale = total
                        create_in = now.strftime('%d/%m/%Y')
                        sale_products = products.copy()

                        sale = Sale(
                            sale_id,
                            seller_id,
                            seller_name,
                            total_sale,
                            create_in,
                            sale_products
                        )
                        sucess = True
                        for product in products:
                            p = Product.return_product_obj(product["name"],product["id"])
                            if not p or p.quantity < product["quantity"]:
                                sucess = False
                                break
                        if sucess:
                            for product in products:
                                p = Product.return_product_obj(product["name"],product["id"])
                                p.remove_stock(product["quantity"])
                                if p.quantity == 0:
                                    p.status = "inactive"

                            append_file('sales.json',sale.__dict__)
                            products.clear()
                            total = 0.0
                            print("Venda finalizada com sucesso!")
                        else:
                            print("Não foi possivel concluir a venda")

                case 3:
                    break

    def seller_menu(self):
        while True:
            now = datetime.now()
            print("-" * 50)
            print(" " * 20 + "Painel de vendas" + " " * 20)
            print("-" * 50)
            print(f"Bem vindo {self.name}")
            print(f"data:{now.strftime('%d/%m/%Y')}")
            print("[1] Criar venda\n[2] Sair")

            try:
                option = int(input("> "))
            except ValueError:
                print("Digite um valor valido")
                continue

            match option:
                case 1:
                    self.create_sale()
                case 2:
                    break
                case _:
                    print("Digite uma opção valida")
from products import Product
from files import return_data,append_file,save_file,generate_id
from seller import Seller

class Admin:
    def __init__(self,name,password,admin_id=None):
        self.name = name
        self.password = password
        self.admin_id = admin_id
        self.profile = "admin"
    
    def create_product_admin(self):
        product = Product.create_product()
        append_file('products.json',product.__dict__)

    def edit_product(self,id,name,attribute,new_attribute):
        products = return_data('products.json')
        found = False

        if products:
            for product in products:
                if (product["product_id"] == id) or (product["name"] == name):
                    if attribute in product:
                        product[attribute] = new_attribute
                        found = True
                    else:
                        return "Atributo invalido"
                    
            if not found:
                return "Produto não encontrado"
            
            save_file('products.json',products)
            return "Atributo alterado com sucesso"
        else:
            return "Não existe produtos cadastrados"


    @classmethod
    def create_new_user(cls):

        data_admins = return_data('admin_users.json')
        data_sellers = return_data('seller_users.json')
        users = data_admins + data_sellers
        
        name = input("Digite o nome do novo usuario: ")
        password = input("Digite uma senha: ")
        print("[1] Administrador\n[2] Vendedor")

        try:
            option = int(input(f"O que o usuario {name} será?: "))
        except ValueError:
            print("Digite um numero correspondente")

        for user in users:
            if user["password"] == password:
                return "Ja existe um usuario com essa senha"

        if option == 1:
            admin = cls(name,password)
            admin.admin_id = generate_id("admin_users.json","admin_id")
            append_file('admin_users.json',admin.__dict__)
            return f"Administrador {admin.name} criado com sucesso."

        elif option == 2:
            seller = Seller(name,password)
            seller.seller_id = generate_id("seller_users.json","seller_id")
            append_file('seller_users.json',seller.__dict__)
            return f"Vendedor {seller.name} criado com sucesso."
        else:
            return "Resposta invalida"
        
    def admin_menu(self):
        while True:
            print("-" * 50)
            print(" " * 20 + "Admin painel" + " " * 20)
            print("-" * 50)
            print(f"Bem vindo {self.name}")
            print("[1] Criar produto\n[2] Editar/inativar produto\n[3] Create new user\n[4] Sair")

            try:
                option = int(input("> "))
            except ValueError:
                print("Digite um valor valido")

            match option:
                case 1:
                    self.create_product_admin()
                case 2:
                    id = int(input("Digite o id do produto: "))
                    name = input("Digite o nome do produto: ")
                    attribute = input("Qual atributo deseja alterar? (name,price,quantity,status): ")
                    new_atribbute = input(f"Digite um novo atributo para {attribute}: ")
                    self.edit_product(id,name,attribute,new_atribbute)
                case 3:
                    Admin.create_new_user()
                case 4:
                    break
                case _:
                    print("Digite uma opção valida")
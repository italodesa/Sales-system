from products import Product
from files import return_data,write_file,generate_id
from seller import Seller

class Admin:
    def __init__(self,name,password,admin_id=None):
        self.name = name
        self.password = password
        self.admin_id = admin_id
        self.profile = "admin"
    
    def create_product_admin(self):
        product = Product.create_product()
        write_file('products.json',product.__dict__)

    @classmethod
    def create_new_user(cls):

        data_admins = return_data('admin_users.json')
        data_sellers = return_data('seller_users.json')
        
        name = input("Digite o nome do novo usuario: ")
        password = input("Digite uma senha: ")
        print("[1] Administrador\n[2] Vendedor")
        option = int(input(f"O que o usuario {name} será?: "))

        if option == 1:
            for admin in data_admins:
                if admin["password"] == password:
                    return "Ja existe um administrador com essa senha"
            admin = cls(name,password)
            admin.admin_id = generate_id("admin_users.json","admin_id")
            write_file('admin_users.json',admin.__dict__)
            return f"Administrador {admin.name} criado com sucesso."

        elif option == 2:
            for seller in data_sellers:
                if seller["password"] == password:
                    return "Já existe um vendedor com essa senha"
            seller = Seller(name,password)
            seller.seller_id = generate_id("seller_users.json","seller_id")
            write_file('seller_users.json',seller.__dict__)
            return f"Vendedor {seller.name} criado com sucesso."
        else:
            return "Resposta invalida"
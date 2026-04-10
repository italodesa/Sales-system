from files import return_data
from admin import Admin
from seller import Seller
def login_menu():
    users = return_data("admin_users.json") + return_data("seller_users.json")
    print("#" * 50)
    print(" " * 20 + "Login" + " " * 20)
    print("#" * 50)
    name = input("Digite seu nome: ")
    password = input("Digite sua senha: ")

    if users:
        for user in users:
            if (name == user["name"]) and (password == user["password"]):
                return user
        print("Usuario não cadastrado")
        return None
    else:
        print("Não existe nenhum usuario cadastrado")
        return None
    
def main_menu():
    while True:
        user = login_menu()
        if user is None:
            continue

        if user["profile"] == "admin":
            admin = Admin(
                user["name"],
                user["password"],
                user["admin_id"],
            )
            admin.admin_menu()

        if user["profile"] == "seller":
            seller = Seller(
                user["name"],
                user["password"],
                user["seller_id"],
            )
            seller.seller_menu()
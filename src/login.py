from files import return_data
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
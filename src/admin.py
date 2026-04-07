from products import Product
from files import return_data,write_file
class Admin:
    def __init__(self,name,password,admin_id=None):
        self.name = name
        self.password = password
        self.admin_id = admin_id
        self.profile = "admin"
    
    def create_product_admin(self):
        product = Product.create_product()
        write_file('products.json',product.__dict__)
from File_handling import storage   

class ProductManagement:
    def add_product(self, product_name, product_price, product_quantity):
        product_id = storage.save_product(product_name, product_price, product_quantity)
        if product_id:
            return True
        return False

    def view_stock(self):
        return storage.get_products() 

    def remove_product(self, product_id):
        return storage.delete_product(product_id) 

class CustomerManagement:
    def buy_product(self, customer_id, product_id, quantity):
        self.order_id = storage.save_order(customer_id, product_id, quantity)
        if self.order_id:
            return True
        return False

    def view_order(self, customer_id):
        return storage.get_order(customer_id)

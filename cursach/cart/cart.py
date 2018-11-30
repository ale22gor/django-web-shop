from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):
    
    def __init__(self, request):
        """
        Initalize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity,  update_quantity=False):
        product_id = str(product.id)
        product_name = product.Name
        price = str(product.Price)
        if product_id not in self.cart:
            print("popalsya")
            self.cart[product_id] = { 'id':product_id, 'name':product_name,'quantity':0, 'price':price}
        if update_quantity:     
            print("update")
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            print("add")
            self.cart[product_id]['quantity'] += int(quantity)
        print(self.cart)
        self.save()
            
    def save(self):
        # update the session cart
        print(self.cart)
        self.session[settings.CART_SESSION_ID] = self.cart
         # mark the session as "modified" to make sure it is saved
        self.session.modified = True
        print(self.cart)

        
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
           
        
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        # get the product objects and add them to the cart
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def __len__(self):
        """
        Count all items in the cart.
        """
        
        return sum(item['quantity'] for item in self.cart.values())
        
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
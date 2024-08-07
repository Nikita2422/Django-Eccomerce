from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the Current session key if it exists
        cart = self.session.get('session_key')

        # if the user is new , no session key! create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is avaialble on all pages of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get ids from cart
        product_ids= self.cart.keys() 
        # Use ids to lookup products in database model
        products = Product.objects.filter(id_in= product_ids)
        # Return those Products
        return products
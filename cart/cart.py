from django.shortcuts import get_list_or_404, get_object_or_404
try:
    from importlib import import_module
except ImportError:
	from django.utils.importlib import import_module


class CartItem(object):
	"""
	A cart Item represents the associated product product with its quantity
	"""

	def __init__(self, product, quantity=1):
		self.product = product
		self.quantity = int(quantity)

	def __repr__(self):
		return u'CartItem object (%s)' % self.product

	def to_dict(self):
		return {
				'product_pk' : self.product.pk,
				'quantity' : self.quantity

		}


	@property
	def subtotal(self):
		"""
		Sub total for the cart item
		"""

		return self.product.price*self.quantity


class Cart(object):
	"""
	A cart that lives in the session
	"""

	def __init__(self, session, session_key=None):
		self._items_dict = {}
		self.session = session
		self.session_key = session_key or 'CART'

			#if a cart representation was previously stored in the session then we
		if self.session_key in self.session:
			#rebuild the cart object from that serialized representation
			cart_representation = self.session[self.session_key]
			ids_in_cart = cart_representation.keys()
			products_queryset = self.get_queryset().filter(pk__in = ids_in_cart)
			for product in products_queryset:
				item = cart_representation[str(product.pk)]
				self._items_dict[product.pk] = CartItem(product, item['quantity'])

	def __contains__(self, product):

		"""
		Checks if the given product is in the cart.
		"""

		return product in self.products




	def get_queryset(self):
		CART_PRODUCT_MODEL='consultation.models.Item'
		package, module = CART_PRODUCT_MODEL.rsplit('.', 1)
		product_model = getattr(import_module(package), module)
		queryset = product_model._default_manager.all()

		return queryset

	def update_session(self):
		"""
		Serializes the cart data, saves it to session and marks session as modified.
		"""
		self.session[self.session_key] = self.cart_serializable
		self.session.modified = True

	def add(self, product, quantity=1):
		"""
		Adds or creates products in cart. For an existing product,
		the quantity is increased and the price is ignored.
		"""
		quantity = 1
		if quantity < 1:
			raise ValueError('Quantity must be at least 1 when adding to cart')
		if product in self.products:
			raise ValueError('Deja dans le panier')
		else:
			self._items_dict[product.pk] = CartItem(product, quantity)
		self.update_session()



	def remove(self, product):
		"""
		Removes the product.
		"""
		if product in self.products:
			del self._items_dict[product.pk]
			self.update_session()

	def clear(self):
		"""
		Removes all items.
		"""
		self._items_dict = {}
		self.update_session()



	@property
	def items(self):
		"""
		The list of cart items.
		"""
		return self._items_dict.values()


	@property
	def cart_serializable(self):
		"""
		The serializable representation of the cart.
		For instance:
		{
			'1': {'product_pk': 1, price: '9.99'},
			'2': {'product_pk': 2, price: '29.99'},
		}
		Note how the product pk servers as the dictionary key.
		"""
		cart_representation = {}
		for item in self.items:
			# JSON serialization: object attribute should be a string
			product_id = str(item.product.pk)
			cart_representation[product_id] = item.to_dict()
		return cart_representation



	@property
	def items_serializable(self):
		"""
		The list of items formatted for serialization.
		"""
		return self.cart_serializable.items()

	@property
	def count(self):
		"""
		The number of items in cart, that's the sum of quantities.
		"""
		return sum([item.quantity for item in self.items])


	@property
	def unique_count(self):
		"""
		The number of unique items in cart, regardless of the quantity.
		"""
		return len(self._items_dict)

	@property
	def is_empty(self):
		return self.unique_count == 0

	@property
	def products(self):
		"""
		The list of associated products.
		"""
		return [item.product for item in self.items]


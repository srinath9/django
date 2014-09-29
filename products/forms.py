from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ("title","description","sale_price","price")
		#exclude =('user',)
		#exclude has to be a tuple there comma 
		#or we can give fields = ("title","sale_price")
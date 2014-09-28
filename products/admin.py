from django.contrib import admin
from .models import Product
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','description','current_price','order')  #list_displlay is inside variable for displaying the connetn in admin page
	#its calling list of functions to perfom
	class Meta:
		model = Product

	def current_price(self,obj):
		if obj.sale_price >0:
			return obj.sale_price
		else :
			return obj.price

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(CategoryAdmin)
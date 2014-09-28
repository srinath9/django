from django.contrib import admin
from .models import Product,Category, Tag, ProductImage, CategoryImage
# Register your models here.

class TagInLine(admin.TabularInline):
	prepopulated_fields = {"slug":('tag',)}
	extra = 1 #these are the number of field availble for input
	model = Tag

class ProductImageInLine(admin.TabularInline):
	model = ProductImage
class CategoryImageInLine(admin.TabularInline):
	model = CategoryImage
#inline should be above just like  c lang

class ProductAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','description','current_price','order','categories','live_links')  
	#list_displlay is inside variable for displaying the connetn in admin page
	#its calling list of functions to perfom
	inlines = [TagInLine, ProductImageInLine]
	search_fields = ['title','price','description','category__title','category__description']
	list_filter = ['price','timestamp','updated']
	#if we change inline to iline then there is no error but no output of these tag lines
	prepopulated_fields = {"slug":('title',)}
	#prepopulated_fields has to be in tuples and hence keep the commas otherwise error will apper
	readonly_fields = ['categories','live_links','description']
#	fields = ['title','slug','live_links']
	class Meta:
		model = Product

	def current_price(self,obj):
		if obj.sale_price >0:
			return obj.sale_price
		else :
			return obj.price
	def categories(self,obj):
		cat = []
		for i in obj.category_set.all():
			link = "<a href='/admin/products/category/" +str(i.id) +"'>" + i.title+ "</a>"
			cat.append(link)
		return ", ".join(cat)
	

	def live_links(self,obj):
		link = "<a href='/products/"+obj.slug + "'>"+obj.title+"</a>"
		return link
	categories.allow_tags = True
	live_links.allow_tags = True
	#we have to mention allowing tags to each function

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":('title',)}
	inlines = [CategoryImageInLine]
	class Meta:
		model = Category

admin.site.register(Category,CategoryAdmin)
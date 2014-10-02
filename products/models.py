from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
	"""docstring for Product"""
	user = models.ForeignKey(User, null = True, blank = True)  #not caring the sec and third paramenters
	title = models.CharField(max_length = 180)
	description = models.CharField(max_length = 500)
	price = models.DecimalField(max_digits=20, decimal_places = 2)
	sale_price = models.DecimalField(max_digits=20, decimal_places = 2,null = True, blank=True)	
	slug = models.SlugField()	
	order = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)

	def __unicode__(self):
		return str(self.title)

	class Meta:
		ordering = ['-order']

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to="product/image/")
	title = models.CharField(max_length=20)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		return str(self.title)

class Tag(models.Model):
	product = models.ForeignKey(Product)
	tag = models.CharField(max_length=20)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		return str(self.tag)

class Category(models.Model):
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length = 180)
	description = models.CharField(max_length = 500)
	slug = models.SlugField()	
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		return str(self.title)

	class Meta:
		verbose_name= "Category"
		verbose_name_plural ="Categories"

class CategoryImage(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to="product/image/")
	title = models.CharField(max_length=20)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		return str(self.title)


class accounts(object):
	"""docstring for accounts"""
	user_name = models.CharField(Product)
	email = models.EmailField(max_length = 180)
	password = models.CharField(max_length = 500)

class fileupload(models.Model):
	files = models.FileField(upload_to="product/image")
	
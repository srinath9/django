from django.db import models
from django.conntrib.auth.models import User
# Create your models here.

class Product(models.Model):
	"""docstring for Product"""
	user = model.ForiegnKey(User, null = True, blank = True)  #not caring the sec and third paramenters
	title = models.CharField(max_length = 180)
	description = models.CharField(max_length = 500)
	price = models.DecimalField(max_digits=20, decimal_places = 2)
	sale_price = models.DecimalField(max_digits=20, decimal_places = 2,null = True, blank=True)	
	slug = models.SlugField()	
	timestamp = models.DateTimeField(auto_now_add = True, aut_now = False)
	updated = models.DateTimeField(auto_now_add = False, aut_now = True)

	def __unicode__(self):
		return str(self..title)


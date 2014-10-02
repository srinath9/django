from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, ProductImage, fileupload
from django import forms

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ("title","description","sale_price","price")
		#exclude =('user',)
		#exclude has to be a tuple there comma 
		#or we can give fields = ("title","sale_price")

class ProductImageForm(ModelForm):
	class Meta:
		model = ProductImage
		

class MyRegistration(UserCreationForm):
	email = forms.EmailField(required = True)	

	class Meta():
		model = User 
		fields = ('username', 'email')

	def save(self,commit=True):
		user = super(UserCreationForm,self).save(commit = False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class file_upload_form(forms.ModelForm):
	class Meta:
		model = fileupload
		

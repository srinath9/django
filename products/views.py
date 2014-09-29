from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.template.defaultfilters import slugify
# Create your views here.
from .models import Product, Category, ProductImage
from forms import ProductForm

def list_all(request):
	products = Product.objects.filter(active = True)

	return render_to_response("products/all.html", locals(), context_instance=RequestContext(request))

def add_product(request):
	form = ProductForm(None) 
	#this make to appear the pre-existing values of each form
	if request.POST:
		
		form = ProductForm(request.POST) 
		if form.is_valid():
			product = form.save(commit=False)
			product.user = request.user
			product.slug = slugify(form.cleaned_data['title'])
			product.active = False
			#converting the title to slug
			product_edit = form.save()
			return HttpResponseRedirect('/products/%s'%product.slug)
	

	return render_to_response("products/edit.html", locals(), context_instance=RequestContext(request))


def edit_product(request,slug):
	instance = Product.objects.get(slug=slug)
	form = ProductForm(None, instance = instance) 
	#this make to appear the pre-existing values of each form
	if request.POST:
		
		form = ProductForm(request.POST, instance = instance) 
		if form.is_valid():
			product_edit = form.save(commit=False)
			product_edit = form.save()
		else:
			print "error"

	if request.user == instance.user:
		return render_to_response("products/edit.html",locals(),context_instance=RequestContext(request))
	else:
		raise Http404

	

def single(request,slug):
	print slug
	product = Product.objects.get(slug=slug)

	images1 =product.productimage_set.all()
	
	if request.user == product.user:

		categories = product.category_set.all()

		context = {
		"product":product,
		"categories" : categories,
		"edit":True,
		
		"images2":images1,
		}
		

		return render_to_response("products/single.html", context, context_instance=RequestContext(request))

	else:
		categories = product.category_set.all()

		context = {
		"product":product,
		"categories" : categories,
		
		"images2":images1,
		}
		return render_to_response("products/single.html",context, context_instance=RequestContext(request))

from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.template.defaultfilters import slugify
# Create your views here.
from .models import Product, Category, ProductImage
from forms import ProductForm,ProductImageForm, MyRegistration, file_upload_form
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth

def register_user(request):
	if request.POST :
		print "post"
		form = MyRegistration(request.POST)
		print form
		if form.is_valid():
			print "save"
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

		else:
			print "error"

	args ={}
	print args
	args.update(csrf(request))

	args['form'] = MyRegistration()
	print args
	return render_to_response('products/register.html',args)


def register_success(request):
	return render_to_response('products/register_success.html')


def login_user(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("products/login.html",c)

def auth_view(request):
	username = request.POST.get('username','')
	
	password = request.POST.get('password','')

	user = auth.authenticate(username = username, password = password)
	
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect("/accounts/login_success")
	else:
		return HttpResponseRedirect("/accounts/invalid")

def loggin_success(request):
	return render_to_response('products/loggedin.html',
		{'full_name':request.user.username})


def invalid(request):
	return render_to_response("products/invalid.html")

def logout(request):
	auth.logout(request)
	return render_to_response("products/loggout.html")


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

def manage_product_image(request,slug):

	try:
		product = Product.objects.get(slug=slug)
	except:
		product = False

	if request.user == product.user:
		form = ProductImageForm(None,instance = product)

		if request.POST:
			form = ProductImageForm(request.POST,instance = product)
			if form.is_valid:
				print "form is valid"

			return render_to_response("products/edit.html",locals(),context_instance=RequestContext(request))

	else:
		raise Http404



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


def file_upload(request):
	if request.POST:
		form = file_upload_form(request.POST,request.FILES)
		if form.is_valid:
			form.save()

	args ={}
	args.update(csrf(request))

	args['form'] = file_upload_form
	print args
	return render_to_response('products/file_upload.html',args)
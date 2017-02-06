from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse

def index(request):
	#context_dict = {'boldmessage': "Andy waz ere"}
	category_list = Category.objects.order_by("-likes")[:5]
	context_dict = {'categories': category_list}
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	print (request.method)
	print (request.user)
	return render(request, 'rango/about.html',{})


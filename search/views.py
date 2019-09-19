from django.shortcuts import render, reverse, redirect
from products.models import Product
from django.contrib import messages


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if products:
        return render(request, "products.html", {"products": products})
    else:
        messages.error(request, "No Results")
        return redirect(reverse('products'))



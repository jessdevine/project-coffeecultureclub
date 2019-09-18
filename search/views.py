from django.shortcuts import render, reverse, redirect
from products.models import Product
from django.contrib import messages
from django.db.models import Count

# Results.objects.filter(event=some_event).annotate(Count('category'), distinct=True)

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if products:
        return render(request, "products.html", {"products": products})
    else:
        messages.error(request, "No Results")
        return redirect(reverse('products'))



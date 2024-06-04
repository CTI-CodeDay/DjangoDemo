from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.
def product_create_view(request):
    form = RawProductForm()
    if(request.method == 'POST'):
        my_form = RawProductForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'products/product_form.html', context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
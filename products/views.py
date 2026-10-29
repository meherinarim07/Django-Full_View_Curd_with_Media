from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def products(request):
    p_list=Product.objects.all()
    return render(request,'products/products.html',{'products':p_list})

def product_create(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
        return render(request,'products/product_create.html',{'form':form})

def product_update(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form=ProductForm(instance=product)
        return render(request,'products/product_update.html',{'form':form})

def product_delete(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('products')
    return render(request,'products/product_delete.html',{'product':product})


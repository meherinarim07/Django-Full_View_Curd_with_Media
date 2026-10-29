from django.shortcuts import render,redirect,get_object_or_404
from .models import Order
from .forms import OrderForm
from products.models import Product
# Create your views here.
def orders(request):
    o_list=Order.objects.all()
    return render(request,'orders/orders.html',{'orders':o_list})

def order_create(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.product=product
            order.save()
            return redirect('orders')
    else:
        form=OrderForm()
    return render(request,'orders/order_create.html',{'form':form,'product':product})

def order_update(request,pk):
    order=get_object_or_404(Order,pk=pk)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form=OrderForm(instance=order)
    return render(request, 'orders/order_update.html', {'form': form, 'order': order})


def order_delete(request,pk):
    order=get_object_or_404(Order,pk=pk)
    if request.method=='POST':
        order.delete()
        return redirect('orders')
    return render(request,'orders/order_delete.html',{'order':order})

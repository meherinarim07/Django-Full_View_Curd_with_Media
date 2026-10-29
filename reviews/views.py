from django.shortcuts import render,redirect,get_object_or_404
from . models import Review
from . forms import ReviewForm
# Create your views here.
def reviews(request):
    r_list=Review.objects.all()
    return render(request,'reviews/reviews.html',{'reviews':r_list})

def review_create(request):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form=ReviewForm()
    return render(request,'reviews/review_create.html',{'form':form})

def review_update(request,pk):
    review=get_object_or_404(Review,pk=pk)
    if request.method=='POST':
        form=ReviewForm(request.POST,instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form=ReviewForm(instance=review)
    return render(request,'reviews/review_update.html',{'form':form})

def review_delete(request,pk):
    review=get_object_or_404(Review,pk=pk)
    if request.method=='POST':
        review.delete()
        return redirect('reviews')
    return render(request,'reviews/review_delete.html',{'review':review})





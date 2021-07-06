from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    item=Product.objects.all()
    return render(request,'products/home.html',{'item':item})
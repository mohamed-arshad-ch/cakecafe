from django.shortcuts import render,redirect
from django.views import View
from user.models import *

# Create your views here.
class DashBoard(View):
    def get(self, request):
        try:
            return render(request,'admin/index.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class AddCategory(View):
    def get(self, request):
        try:
            category = Category.objects.all()
            index = {
                "categorys":category
            }
            return render(request,'admin/add-category.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    def post(self, request):
        try:
            category, created = Category.objects.get_or_create(title=request.POST['category'])
            return redirect("category")
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class AddProduct(View):
    def get(self, request):
        try:
            category = Products.objects.all()
            index = {
                "categorys":category
            }
            return render(request,'admin/add-product.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    def post(self, request):
        try:
            product, created = Products.objects.get_or_create(name=request.POST['name'],price=request.POST['price'],stock=request.POST['stock'],weight=request.POST['weight'],image=request.FILES.get('image'))
            return redirect("product")
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
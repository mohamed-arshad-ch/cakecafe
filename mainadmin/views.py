from django.shortcuts import render,redirect
from django.views import View
from user.models import *
import json
from django.core import serializers
from django.http import JsonResponse
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
            product = Products.objects.all()
            category = Category.objects.all()
            index = {
                "products":product,
                "categorys":category
            }
            return render(request,'admin/add-product.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    def post(self, request):
        try:
            category = Category.objects.get(title=request.POST['category'])
            product, created = Products.objects.get_or_create(name=request.POST['name'],price=request.POST['price'],stock=request.POST['stock'],weight=request.POST['weight'],image=request.FILES.get('image'),category=category,unit=request.POST['unit'])
            return redirect("product")
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class FetchProduct(View):
    def get(self, request,id):
        try:
             
            
            
            qs_json = serializers.serialize('json', Products.objects.filter(id=id))
            
            return JsonResponse(qs_json,safe=False)
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class EditProduct(View):
    def post(self,request,id):
        try:
            product = Products.objects.get(id=id)
            category = Category.objects.get(title=request.POST['categoryedit'])
            product.name = request.POST['nameedit']
            product.price = request.POST['priceedit']
            product.stock = request.POST['stockedit']
            product.weight = request.POST['weightedit']
            product.unit = request.POST['unitedit']
            product.category = category
            product.save()
            return redirect("product")

            
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class DeleteProduct(View):
    def post(self,request,id):
        try:
            product = Products.objects.get(id=id).delete()
            
            return redirect("product")

            
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
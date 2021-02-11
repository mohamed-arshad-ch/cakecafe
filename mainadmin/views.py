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
            image = request.FILES.get('imageedit')
            if image == None:

            
                product.name = request.POST['nameedit']
                product.price = request.POST['priceedit']
                product.stock = request.POST['stockedit']
                product.weight = request.POST['weightedit']
                product.unit = request.POST['unitedit']
                product.category = category
                product.save()
                
                return redirect("product")
            else:
                product.image = image
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

class EditCategory(View):
    def get(self, request,id):
        try:
             
            
            
            qs_json = serializers.serialize('json', Category.objects.filter(id=id))
            
            return JsonResponse(qs_json,safe=False)
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
    def post(self,request,id):
        try:
            
            category = Category.objects.get(id=id)
            category.title = request.POST['editcategory']
            
            category.save()
            return redirect("category")

            
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class DeleteCategory(View):
    def post(self,request,id):
        try:
            category = Category.objects.get(id=id).delete()
            
            return redirect("category")

            
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class PendingInCart(View):
    def get(self, request):
        try:
            order = Order.objects.filter(status=False)
            
            index = {
                "orders":order
            }
            return render(request,'admin/pending-in-cart.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class PendingCartDetails(View):
    def get(self,request,id):
        try:
            itemdetails = {"itemname":[],"qty":[],"price":[],"total":[]}
            orderitem = OrderItem.objects.filter(order__id=id)
            for items in orderitem:
                itemdetails['itemname'].append(items.product.name)
                itemdetails['qty'].append(items.qty)
                itemdetails['price'].append(items.product.price)
                itemdetails['total'].append(items.subTotal())

            return JsonResponse(itemdetails,safe=False)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class ConfirmOrders(View):
    def get(self, request):
        try:
            order = Order.objects.filter(status=True)
            
            index = {
                "orders":order
            }
            return render(request,'admin/confirmed-orders.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class FetchOrderDetails(View):
    def get(self, request,id):
        try:
            paidamount = ShippingAddress.objects.get(order__id=id)
            
            orderitem = OrderItem.objects.filter(order__id=id)
            itemdetails = {"id":[],"itemname":[],"qty":[],"price":[],"total":[],"status":[],"paidamount":str(paidamount.amount),"subtotal":[]}
            total = 0
            for items in orderitem:
                itemdetails['id'].append(items.id)
                itemdetails['itemname'].append(items.product.name)
                itemdetails['qty'].append(items.qty)
                itemdetails['price'].append(items.product.price)
                itemdetails['total'].append(items.subTotal())
                itemdetails['status'].append(items.track)
                total+= items.subTotal()
                
            itemdetails['subtotal'].append(total)
            return JsonResponse(itemdetails,safe=False)
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class EditOrderStatus(View):
    def get(self, request,id,status):
        try:
            orderitem = OrderItem.objects.get(id=id)
            orderitem.track = status
            orderitem.save()
            return JsonResponse({"message":"Successfully Updated","type":"succ"})
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
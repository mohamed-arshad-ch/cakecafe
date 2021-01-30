from django.shortcuts import render
from django.views import View
# Create your views here.


#Landing Page View
class LandingPage(View):
    
    #Render Landing PAge
    def get(self, request, *args, **kwargs):
        try:
            return render(request,'user/index.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
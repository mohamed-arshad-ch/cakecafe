from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('newcommonadmin/', admin.site.urls),
    
    #User Root Url

    path('',include('user.urls')),

    #Admin Root Url
    path('javas',include('mainadmin.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
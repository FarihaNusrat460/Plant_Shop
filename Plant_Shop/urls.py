"""Plant_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from User import views as user_views
from Product import views as product_views
from Blog import views as Blog_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/',user_views.registration),
    path('Homepage/',product_views.showHome,name='Homepage'),
    path('Product/',product_views.showProducts,name='Product'),
    path('Product/<int:product_id>', product_views.showDetails, name='detail_view'),

    path('ShowBlogs/', Blog_views.showBlog,name='ShowBlogs'),
    path('InsertBlogs/', Blog_views.insertBlog,name='InsertBlogs'),
    path('accounts/',include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

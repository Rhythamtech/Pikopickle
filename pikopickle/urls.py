"""pikopickle URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('cart/',views.cartDetails),
    path('contact/',views.contact),
    path('about-us/',views.about),
    path('disclaimer/',views.disclaimer),
    path('wishlist/',views.wishlist),
    path('delwish/<int:num>/',views.delwish),
    path('addwish/<int:num>/',views.addwishlist),
    path('checkout/',views.checkoutDetails),
    path('login/',views.loginDetails),
    path('logout/',views.logout),
    path('signup/',views.signupDetails),
    # path('shop/<str:cat>/',views.shopDetails),
    path('product/<int:num>/',views.productDetails),
    path('myproduct/',views.myproduct),
    path('editproduct/<int:num>/',views.editproduct),
    path('deleteproduct/<int:num>/',views.deleteproduct),
    path('deletecart/<int:num>/',views.deletecart),
    path('profile/',views.profile),
    path('confirm/',views.confirm),
    path('add/',views.addpickle),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

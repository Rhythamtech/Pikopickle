from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    c=Category.objects.all()
    crt=Cart.objects.all()
    if request.method=="POST":
        s=request.POST.get("search")
        p=Product.objects.filter(Q(name__icontains=s))
    else:
        p=Product.objects.all()
    return render(request,'index.html',
                  {
                      "Category":c,
                      "Product":p,
                      "Cartcount":len(crt),
                  })
@login_required(login_url='/login/')
def cartDetails(request):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        try:
            seller.objects.get(uname=request.user)
            return HttpResponseRedirect('/profile/')
        except:
            b=Buyer.objects.get(uname=request.user)
            c =Cart.objects.filter(buyer=b)
            subtotal = 0
            for i in c:
                subtotal += i.total
            if subtotal<1000:
                delivery=100
            else:
                delivery=0
            finalamt=subtotal+delivery
            return render(request,"cart.html",
                          {
                              "Cart":c,
                              "Delivery":delivery,
                              "FinalAmt":finalamt,
                              "Subtotal":subtotal,
                          })

def deletecart(request,num):
    user=User.objects.get(username=request.user)
    if user.is_superuser :
        return HttpResponseRedirect('/admin/')
    c=Cart.objects.get(id=num)
    c.delete()
    return HttpResponseRedirect('/cart/')

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='/login/')
def productDetails(request,num):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        try:
            seller.objects.get(uname=request.user)
            return HttpResponseRedirect("/profile/")
        except:
            p = Product.objects.get(id=num)
            if request.method == 'POST':
                c = Cart()
                b = Buyer.objects.get(uname=request.user)
                c.buyer = b
                c.product = p
                c.quantity = int(request.POST.get('qty'))
                c.total = p.finalprice * c.quantity
                c.save()
                print("i m added to cart")
                return HttpResponseRedirect("/cart/")
            return render(request,'product.html',
                          {
                              "Product":p
                           })



def checkoutDetails(request):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        try:
            seller.objects.get(uname=request.user)
            return HttpResponseRedirect("/profile/")
        except:
            b=Buyer.objects.get(uname=request.user)
            c=Cart.objects.filter(buyer=b)
            if request.method=="POST":
                ch=Checkout()
                ch.name=request.POST.get("name")
                ch.email=request.POST.get("email")
                ch.address1=request.POST.get("address1")
                ch.address2=request.POST.get("address2")
                ch.state=request.POST.get("state")
                ch.city=request.POST.get("city")
                ch.pin=request.POST.get("pin")
                ch.phone=request.POST.get("phone")
                ch.cart=c[0]
                ch.total=c[0].total
                ch.mode=request.POST.get("option")
                ch.save()
                return HttpResponseRedirect("/confirm/")
            return render(request,"checkout.html",
                          {
                              "Cart":c,
                              "count":len(c),
                              "User":b,
                          })



def loginDetails(request):
    if (request.method=='POST'):
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'login.html')


def signupDetails(request):
    choice = request.POST.get("option")
    if choice == 'seller':
        s=seller()
        s.uname= request.POST.get("uname")
        s.name= request.POST.get("name")
        s.email= request.POST.get("email")
        passwrd=request.POST.get("password")
        try:
            user =User.objects.create_user(username=s.uname,email=s.email,password=passwrd)
            s.save()
            messages.success(request, "Sucessfully Signup")
            return HttpResponseRedirect('/login/')
        except:
            messages.error(request, "User already exist or Invalid credentials !! ")
            return render(request,'login.html')
    else:
        b = Buyer()
        b.uname = request.POST.get("uname")
        b.name = request.POST.get("name")
        b.email = request.POST.get("email")
        passwrd = request.POST.get("password")
        try:
            user = User.objects.create_user(username=b.uname, email=b.email, password=passwrd)
            b.save()
            messages.success(request, "Sucessfully Signup")
            return HttpResponseRedirect('/login/')
        except:
            messages.error(request, "User already exist or Invalid credentials !! ")
            return render(request, 'login.html')

@login_required(login_url='/login/')
def profile(request):
    #code to print data to table line no 55 and 72
    user=User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        try:
            s=seller.objects.get(uname=request.user)
            p=Product.objects.filter(Seller=s)
            #code to save data in database in if condition
            if request.method=='POST':
                s.name=request.POST.get('name')
                s.uname=request.POST.get('uname')
                s.email=request.POST.get('email')
                s.phone=request.POST.get('phone')
                s.bankName =request.POST.get('bank')
                s.ifscCode =request.POST.get('ifsc')
                print("save ifsc")
                s.accountNumber =request.POST.get('account')
                print("save account")
                s.save()
                return HttpResponseRedirect('/profile/')
            return render(request, 'profile.html', {'User': s,})

        except:
            b = Buyer.objects.get(uname=request.user)
            # code to save data in database in if condition
            if request.method == 'POST':
                b.name = request.POST.get('name')
                b.uname = request.POST.get('uname')
                b.email = request.POST.get('email')
                b.phone = request.POST.get('phone')
                b.address1 = request.POST.get('address1')
                b.address2 = request.POST.get('address2')
                b.state = request.POST.get('state')
                b.city = request.POST.get('city')
                b.pin = request.POST.get('pin')
                b.save()
                return HttpResponseRedirect('/profile/')
            return render(request, 'buyerprofile.html', {'User': b})

@login_required(login_url='/login/')
def myproduct(request):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
       try:
           s = seller.objects.get(uname=request.user)
           p = Product.objects.filter(Seller=s)
           return render(request, "myproduct.html", {"Product": p})
       except:
           return HttpResponseRedirect('/')




def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def addpickle(request):
    user = User.objects.get(username=request.user)
    c = Category.objects.all()
    if user.is_superuser :
        return HttpResponseRedirect("/admin/")
    if request.method=="POST":
        s=seller.objects.get(uname=request.user)
        p=Product()
        p.name=request.POST.get('name')
        p.description=request.POST.get('desc')
        p.discount=int(request.POST.get('discount'))
        p.category=Category.objects.get(name=request.POST.get('category'))
        p.baseprice=int(request.POST.get('price'))
        p.finalprice= p.baseprice - p.baseprice*int(p.discount)//100
        p.img1=request.FILES.get('img1')
        p.img2=request.FILES.get('img2')
        p.img3=request.FILES.get('img3')
        p.img4=request.FILES.get('img4')


        p.Seller=s
        p.save()
        return HttpResponseRedirect('/profile/')
    return render(request,'add.html',
                  {
                      "Category":c,
                  })
@login_required(login_url='/login/')
def deleteproduct(request,num):
    user=User.objects.get(username=request.user)
    if user.is_superuser :
        return HttpResponseRedirect('/admin/')

    p=Product.objects.get(id=num)
    p.delete()
    return HttpResponseRedirect('/myproduct/')

@login_required(login_url='/login/')
def wishlist(request):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:

            b=Buyer.objects.get(uname=request.user)
            w =Wishlist.objects.filter(buyer=b)
            return render(request,"wishlist.html",
                  {
                      "W":w,
                  })


@login_required(login_url='/login/')
def delwish(request,num):
    user=User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    wish=Wishlist.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlist/')


@login_required(login_url='/login/')
def addwishlist(request,num):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        try:
            seller.objects.get(uname=request.user)
            return HttpResponseRedirect("/profile/")
        except:
            p = Product.objects.get(id=num)
            w = Wishlist()
            b = Buyer.objects.get(uname=request.user)
            w.buyer = b
            w.product = p
            w.save()
            return HttpResponseRedirect("/wishlist/")


@login_required(login_url='/login/')
def editproduct(request,num):
    user = User.objects.get(username=request.user)
    c = Category.objects.all()
    p = Product.objects.get(id=num)

    if user.is_superuser:
        return HttpResponseRedirect("/admin/")
    if request.method == "POST":
        s = seller.objects.get(uname=request.user)
        p.name = request.POST.get('name')
        p.description = request.POST.get('desc')
        p.discount = int(request.POST.get('discount'))
        p.category = Category.objects.get(name=request.POST.get('category'))
        p.baseprice = int(request.POST.get('price'))
        p.finalprice = p.baseprice - p.baseprice * int(p.discount) // 100


        if (not request.FILES.get('img1') == None):
            p.img1 = request.FILES.get('img1')
        if (not request.FILES.get('img2') == None):
            p.img2 = request.FILES.get('img2')
        if (not request.FILES.get('img3') == None):
            p.img3 = request.FILES.get('img3')
        if (not request.FILES.get('img4') == None):
            p.img4 = request.FILES.get('img4')
        if request.POST.get("stock")=="2":
            p.stock=True

        p.Seller = s
        p.save()
        return HttpResponseRedirect('/profile/')
    return render(request, 'editproduct.html',
                  {
                      "Category": c,
                      "Product":p,
                  })
def confirm(request):
    return render(request,"confirm.html")
def about(request):
    return render(request,"about-us.html")
def disclaimer(request):
    return render(request,"disclaimer.html")

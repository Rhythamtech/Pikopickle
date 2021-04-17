from django.db import models

class seller(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=20)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=15,default=None,null=True,blank=True)
    bankName=models.CharField(max_length=15,default=None,null=True,blank=True)
    ifscCode=models.CharField(max_length=15,default=None,null=True,blank=True)
    accountNumber=models.CharField(max_length=15,default=None,null=True,blank=True)
    total=models.IntegerField(default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name


class Buyer(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=20)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=15,default=None,null=True,blank=True)
    address1=models.CharField(max_length=15,default=None,null=True,blank=True)
    address2=models.CharField(max_length=25,default=None,null=True,blank=True)
    address2=models.CharField(max_length=25,default=None,null=True,blank=True)
    state=models.CharField(max_length=15,default=None,null=True,blank=True)
    city=models.CharField(max_length=15,default=None,null=True,blank=True)
    pin=models.CharField(max_length=10,default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.id)+" "+self.name

class Product(models.Model):
    stock=models.BooleanField(default=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    baseprice=models.IntegerField(default=None,null=True,blank=True)
    finalprice=models.IntegerField(default=None,null=True,blank=True)
    discount=models.IntegerField(default=None,null=True,blank=True)
    Seller=models.ForeignKey(seller,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    img3 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    img4 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Cart(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    def __str__(self):
        return str(self.id)+" "+self.buyer.name

class Wishlist(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Checkout(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    total=models.IntegerField()
    name=models.CharField(max_length=20,default=None)
    phone=models.CharField(max_length=20,default=None)
    email=models.CharField(max_length=20,default=None)
    address1=models.CharField(max_length=30)
    address2=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin=models.CharField(max_length=30)
    mode=models.CharField(max_length=30,default=None)

    def __str__(self):
        return str(self.id)

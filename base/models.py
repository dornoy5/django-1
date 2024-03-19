from django.contrib.auth.models import User
from django.db import models

# --------------------------------------------------------------------------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
# --------------------------------------------------------------------------------------------------------------------
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')), null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
# -------------------------------------------------------------------------------------------------------------------- 
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
# --------------------------------------------------------------------------------------------------------------------
class Product(models.Model):
    desc = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdTime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.desc

# -------------------------------------------------------------------------------------------------------------------- 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
# --------------------------------------------------------------------------------------------------------------------
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order.id} - {self.product.desc}"
# --------------------------------------------------------------------------------------------------------------------
class CartItem(models.Model):
    session_key = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart {self.session_key} - {self.product.desc}"

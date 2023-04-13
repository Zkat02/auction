from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=8,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    business_address = models.CharField(max_length=100)
    business_phone_number = models.CharField(max_length=8)
    business_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_description = models.TextField(blank=True)
    product_image = models.ImageField()
    product_price = models.DecimalField(decimal_places=2,max_digits=7)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + self.vendor

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Auction(models.Model):
    auction_id = models.AutoField(primary_key=True, unique=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)  # (foreign key referencing Products table)
    auction_start_time = models.DateTimeField(null=False)
    auction_end_time = models.DateTimeField(null=False)
    start_bid_price = models.DecimalField(null=False,decimal_places=2,max_digits=7)
    current_bid_price = models.DecimalField(null=False,decimal_places=2,max_digits=7)
    current_bidder_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # (foreign key referencing Users table)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auction_id + self.product

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'


class Bid(models.Model):
    """

    |----------------------------------------|
    |                 ставка                 |
    |----------------------------------------|
    | bid_id -- PK                           |
    | auction_id -- FK referencing Auctions  |
    | user_id -- FK referencing Users        |
    | bid_amount -- value                    |
    | date_created                           |
    |----------------------------------------|

    """

    bid_id = models.AutoField(primary_key=True, unique=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bid_value = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auction + self.profile

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

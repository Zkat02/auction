from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    # user_id = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username
    # password
    # email
    # firstname = models.CharField(max_length=30)
    # lastname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True)


class Vendors(models.Model):
    vendor_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    business_address = models.CharField(max_length=100)
    business_phone_number = models.CharField(max_length=8)
    business_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    product_image = models.ImageField()
    product_price = models.DecimalField(decimal_places=2,max_digits=7)
    date_created = models.DateTimeField(auto_now_add=True)


class Auctions(models.Model):
    auction_id = models.AutoField(primary_key=True, unique=True)
    product_id = models.OneToOneField(Products, on_delete=models.CASCADE)  # (foreign key referencing Products table)
    auction_start_time = models.DateTimeField(null=False)
    auction_end_time = models.DateTimeField(null=False)
    start_bid_price = models.DecimalField(null=False,decimal_places=2,max_digits=7)
    current_bid_price = models.DecimalField(null=False,decimal_places=2,max_digits=7)
    current_bidder_id = models.OneToOneField(Users, on_delete=models.CASCADE)  # (foreign key referencing Users table)
    date_created = models.DateTimeField(auto_now_add=True)


class Bids(models.Model):
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
    auction_id = models.ForeignKey(Auctions, on_delete=models.CASCADE)
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    bid_value = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

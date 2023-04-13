from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import *


class Profile_Admin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Profile, Profile_Admin)


class Vendor_Admin(admin.ModelAdmin):
    list_display = ('vendor_id', 'profile', 'business_name', 'country', 'city', 'business_email')
    list_display_links = ('vendor_id', 'business_name',)
    search_fields = ('business_name', 'country', 'city', 'business_email')
    list_filter = ('profile', 'country',
                   'city')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Vendor, Vendor_Admin)


class Product_Admin(admin.ModelAdmin):
    list_display = ('product_id', 'vendor', 'product_name', 'product_price', 'date_created')
    list_display_links = ('product_id', 'product_name')
    search_fields = ('product_name', 'product_price', 'date_created')
    list_filter = ('vendor', 'product_name', 'product_price',
                   'date_created')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Product, Product_Admin)


class Auction_Admin(admin.ModelAdmin):
    list_display = (
    'auction_id', 'product', 'auction_start_time', 'auction_end_time', 'start_bid_price', 'current_bid_price')
    list_display_links = ('auction_id', 'product')
    search_fields = ('auction_start_time', 'auction_end_time', 'start_bid_price', 'current_bid_price')
    list_filter = ('product', 'auction_start_time', 'auction_end_time', 'start_bid_price',
                   'current_bid_price')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Auction, Auction_Admin)


class Bid_Admin(admin.ModelAdmin):
    list_display = ('bid_id', 'auction', 'profile', 'bid_value', 'date_created')
    list_display_links = ('bid_id', 'auction', 'profile')
    search_fields = ('auction_id', 'profile', 'bid_value', 'date_created')
    list_filter = ('auction', 'profile', 'bid_value',
                   'date_created')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Bid, Bid_Admin)



from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import *


class Users_Admin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)

    # list_display = ('user_id','User')#, 'User.name', 'User.email')
    # list_display_links = ('user_id',)
    # search_fields = ('user_id',)
    # list_filter = ('user_id',)  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Users, Users_Admin)


class Vendors_Admin(admin.ModelAdmin):
    list_display = ('vendor_id', 'user_id', 'business_name', 'country', 'city', 'business_email')
    list_display_links = ('vendor_id', 'business_name',)
    search_fields = ('business_name', 'country', 'city', 'business_email')
    list_filter = ('user_id', 'country',
                   'city')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Vendors, Vendors_Admin)


class Products_Admin(admin.ModelAdmin):
    list_display = ('product_id', 'vendor_id', 'product_name', 'product_price', 'date_created')
    list_display_links = ('product_id', 'product_name')
    search_fields = ('product_name', 'product_price', 'date_created')
    list_filter = ('vendor_id', 'product_name', 'product_price',
                   'date_created')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Products, Products_Admin)


class Auctions_Admin(admin.ModelAdmin):
    list_display = (
    'auction_id', 'product_id', 'auction_start_time', 'auction_end_time', 'start_bid_price', 'current_bid_price')
    list_display_links = ('auction_id', 'product_id')
    search_fields = ('auction_start_time', 'auction_end_time', 'start_bid_price', 'current_bid_price')
    list_filter = ('product_id', 'auction_start_time', 'auction_end_time', 'start_bid_price',
                   'current_bid_price')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Auctions, Auctions_Admin)


class Bids_Admin(admin.ModelAdmin):
    list_display = ('bid_id', 'auction_id', 'user_id', 'bid_value', 'date_created')
    list_display_links = ('bid_id', 'auction_id', 'user_id')
    search_fields = ('auction_id', 'user_id', 'bid_value', 'date_created')
    list_filter = ('auction_id', 'user_id', 'bid_value',
                   'date_created')  # создаёт фильтр по этим значениям. Которым можно пользоваться в админ панели на сайте


admin.site.register(Bids, Bids_Admin)



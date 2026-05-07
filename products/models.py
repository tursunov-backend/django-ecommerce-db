from django.db import models

from django.contrib import User


class Addresses(models.Model):
    user_id = models.BigIntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    parent_id = models.BigIntegerField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    category_id = models.BigIntegerField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImages(models.Model):
    product_id = models.BigIntegerField(max_length=255)
    image_url = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    product_id = models.BigIntegerField(max_length=255)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class Carts(models.Model):
    user_id = models.BigIntegerField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=255)

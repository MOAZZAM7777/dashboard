from django.db import models

# Create your models here.
# models.py


class Employees(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField()
    phone = models.IntegerField(unique=True)
    salary = models.TextField()


def __str__(self):
    return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    phone = models.IntegerField(unique=True)
    Brand = models.TextField()
    quantity = models.IntegerField()
    amount = models.TextField()
    invoiceNumber = models.IntegerField()
    invoiceDate = models.CharField(max_length=10)


def __str__(self):
    return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    colorname = models.CharField(max_length=200, unique=True)
    Category = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    colorcode = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()


def __str__(self):
    return self.name


class Category(models.Model):
    categoryname = models.CharField(max_length=200, unique=True)
    Types = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    colorcode = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()


def __str__(self):
    return self.name


class Supplier(models.Model):
    suppliercode = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    website = models.CharField(max_length=100)
    Notes = models.TextField()


def __str__(self):
    return self.name


class Stock(models.Model):
    Items = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, unique=True)
    Brand = models.CharField(max_length=100, unique=True)
    Status = models.CharField(max_length=100)
    sellingprice = models.IntegerField()


def __str__(self):
    return self.name

from django.db import models

class Role(models.Model):
    title = models.CharField()

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    fio = models.CharField()
    login = models.CharField()
    password = models.CharField()

class Address(models.Model):
    index = models.IntegerField()
    city = models.CharField()
    street = models.CharField()
    house = models.IntegerField()

class Status(models.Model):
    title = models.CharField()

class Order(models.Model):
    date_order = models.DateField()
    date_deliver = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class NameTovar(models.Model):
    title = models.CharField()

class Supplier(models.Model):
    title = models.CharField()

class Producer(models.Model):
    title = models.CharField()

class Category(models.Model):
    title = models.CharField()

class Tovar(models.Model):
    art = models.CharField()
    title = models.ForeignKey(NameTovar, on_delete=models.CASCADE)
    unit = models.CharField()
    price = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.IntegerField()
    amount = models.IntegerField()
    description = models.CharField()
    photo = models.CharField()


class OrderTovar(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    amount = models.IntegerField()
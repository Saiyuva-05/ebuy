from django.db import models

class Dress_product(models.Model):
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Singleproduct')
    price = models.IntegerField()
    offer = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.description


class Electronic_product(models.Model):
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Singleproduct')
    price = models.IntegerField()
    offer = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.description

class Order(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    product = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.CharField(max_length=20)
    quantity=models.IntegerField()

    def __str__(self):
        return self.firstname

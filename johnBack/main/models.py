import os

from django.core.exceptions import ValidationError
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    code = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return f'{self.name}->{self.price}$'




class Extra(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    code = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return f'{self.name}->{self.price}$'


class Product(models.Model):
    VARIANTS  = (
        ('Size','Size'),
        ('Extra','Extra'),

    )
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=False)
    description = models.CharField(max_length=300,blank=False)
    path = models.ImageField(max_length=100,blank=False,upload_to='images')
    size = models.ManyToManyField(Size)
    extra = models.ManyToManyField(Extra)

    def __str__(self):
        return f'{self.category}->{self.name}'





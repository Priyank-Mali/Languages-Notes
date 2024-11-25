from django.db import models
from django.utils import timezone
import string
import random
from django.contrib import messages
from django.core.exceptions import ValidationError

WEIGHTAGE_CHOICE = (
    ('ml','mililiter'),
    ('g','gram')
)

# Create your models here.

def generate_random_product_id():
    character = string.ascii_letters + string.digits 
    password = ""

    for i in range(8):
        password += random.choice(character)
    
    return password


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self,*args,**kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        super(BaseModel,self).save(*args,**kwargs)


class ProductCategory(BaseModel):
    category_id = models.CharField(primary_key=True,blank=True,unique=True,max_length=10)
    category_name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f'{self.category_name} with ID :  {self.category_id}'

    def save(self,*args,**kwargs):
        if not self.pk: 
            self.category_id = generate_random_product_id()

        super(ProductCategory,self).save(*args,**kwargs)

    # def clean(self):
    #     # prevent changes to 'product_id' or any data before saving it
    #     # he clean method is part of Django's model validation framework and can be used to enforce rules before saving data.

    #     if self.pk and self.__class__.objects.filter(pk=self.pk).exists():
    #         original = self.__class__.objects.get(pk=self.pk)
    #         if self.product_id != original.product_id:
    #             raise ValidationError("You can't update the Product ID once it is set.")



class Products(BaseModel):
    PRIFIX = "PROD"
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=255,primary_key=True,blank=True,unique=True)
    product_title = models.CharField(max_length=255,blank=False)
    descreption = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='product-images/',blank=True)
    price = models.DecimalField(max_digits=10,default=0.00,decimal_places=2,blank=True)
    weight = models.DecimalField(max_digits=8,decimal_places=2,default=0.00,blank=True)
    weightage_unit = models.CharField(max_length=10,choices=WEIGHTAGE_CHOICE,default='undefined',blank=True)


    def save(self,*args,**kwargs):
        if not self.pk:
            last_product = Products.objects.order_by('-created_at').first()
            if last_product:
                last_numeric_value = int(last_product.product_id[len(self.PRIFIX):])
                new_numneric_value = last_numeric_value + 1
                new_id = f'{self.PRIFIX}{new_numneric_value:04}'
                
            else:
                new_id = f'{self.PRIFIX}0001'

            self.product_id = new_id
        
        super(Products,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.category.category_name} : {self.product_title}'
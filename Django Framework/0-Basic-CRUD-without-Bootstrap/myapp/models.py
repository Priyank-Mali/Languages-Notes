from django.db import models

# Create your models here.

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(BaseClass):
    name = models.CharField(max_length=20,blank=False,null=False)

    class Meta:
        unique_together = ["name"]

    def __str__(self):
        return self.name

class Mobile(BaseClass):
    PREFIX = "MOB@"
    mobile_id = models.CharField(blank=True,primary_key=True,null=False,max_length=20)
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50,blank=False)
    price = models.FloatField(blank=True,default=0.00)
    image = models.ImageField(upload_to="images/",blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand_name} {self.model_name}"
    
    class Meta:
        unique_together = ["brand_name", "model_name"]

    def save(self):
        if not self.pk:
            last_object = Mobile.objects.order_by("-created_at").first()

            if last_object:
                last_numeric_part = int(last_object.mobile_id[len(self.PREFIX):])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:03}"
            else:
                new_id = f"{self.PREFIX}001"
        
            self.mobile_id = new_id
        
        super(Mobile,self).save()
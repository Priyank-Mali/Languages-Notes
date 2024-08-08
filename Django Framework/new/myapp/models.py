from django.db import models

# Create your models here.

class Fruit(models.Model):
    fruit_name = models.CharField(max_length=100)
    price = models.IntegerField()
    manufacturing_date = models.DateField()
    description = models.TextField()
    is_fresh = models.BooleanField(default=False)


    def __str__(self):
        return self.fruit_name


    """
    This metadata affects the model's behavior in different ways, such as specifying the database table name, ordering of query results, verbose names, and other options. 
    """
    class Meta:
        db_table = "MyFruit"  #  Specifies the name of the database table 
        ordering = ['fruit_name']
        verbose_name = 'My Fruit Model'
        unique_together = ['fruit_name' , 'price']
        # abstract = True
        # permissions = [
        #     ('can_view' , 'Can view the model'),
        #     ('can_edit' , 'Can edit the model'),
        # ]

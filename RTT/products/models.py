from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from user.models import User

# Create your models here.
class Category(MPTTModel):
    """Category model """
    title = models.CharField(max_length=255)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    def __str__(self):
        return self.title
class Product(models.Model):
    """ Product models Fields"""
    title = models.CharField(max_length=128)
    product_id = models.CharField(max_length=10, unique=True)
    discussion = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    sold_number = models.PositiveIntegerField(default=0,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'product_category')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_creator')
    quantity_counter = models.PositiveSmallIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('name',)
    
    def __str__(self) -> str:
        return self.title
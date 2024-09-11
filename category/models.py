# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    priority = models.PositiveIntegerField()
    parent_category = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='category_created_by') 
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="category_modified_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author_created_by') 
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="author_modified_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
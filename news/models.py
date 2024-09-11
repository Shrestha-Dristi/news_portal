from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from author.models import Author

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tags_created_by') 
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="tags_modified_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


# TODO: Add author m2m  field in news

class News(models.Model):
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tags)
    content = models.TextField()
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    author = models.ManyToManyField(Author)
    is_featured = models.BooleanField()
    is_active = models.BooleanField()
    is_published = models.BooleanField()
    is_premium = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='news_created_by') 
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="news_modified_by")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
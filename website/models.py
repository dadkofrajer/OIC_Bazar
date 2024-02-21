from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Category(models.Model):
    categoryName = models.CharField(max_length=30)

User._meta.get_field('groups').remote_field.related_name = 'website_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'website_user_permissions'


class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image_Url = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="listings_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="listings_in_category")

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_review")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing")
    review = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.author} reviewed on {self.listing}"
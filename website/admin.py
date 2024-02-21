from django.contrib import admin
from .models import User, Category, Listing, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Review)


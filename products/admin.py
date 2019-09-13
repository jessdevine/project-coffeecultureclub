from django.contrib import admin
from .models import Product, Review
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Product)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'comment', 'published_date', 'author')
    list_filter = ['published_date']
    search_fields = ['comment']
    
admin.site.register(Review, ReviewAdmin)
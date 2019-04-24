from django.contrib import admin
from .models import NewsUser

# Register your models here.
class NewsletterAmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    
admin.site.register(NewsUser, NewsletterAmin)
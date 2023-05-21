from django.contrib import admin
from .models import HomePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['home_title','home_bg']
    list_display_links = list_display


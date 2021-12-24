from django.contrib import admin

from .models import Realtor

# Creating a class that will change display properties of Realtor in admin site
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

# This will register the Realtor model in the Django admin site
admin.site.register(Realtor, RealtorAdmin)

from django.contrib import admin

from .models import Listing

# Creating a class to change the display properties of Listing in admin site
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # Can go to the listing properties using either id or title
    list_filter = ('realtor',) # Filter by realtor
    list_editable = ('is_published',) # Could be edited via the site
    search_fields = ('title', 'description', 'adress', 'city', 'state', 'zipcode', 'price') # Get a search field
    list_per_page = 25 # Pagination
 
admin.site.register(Listing, ListingAdmin)

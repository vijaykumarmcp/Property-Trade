from django.contrib import admin

from . models import Listings
# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','realtor')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    list_per_page=5
    search_fields=('title','address','city','state','price')



admin.site.register(Listings,ListingsAdmin)
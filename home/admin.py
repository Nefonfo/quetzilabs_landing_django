from django.contrib import admin
from .models import OurOffer

# Register your models here.

class OurOfferAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ('title', 'icon', 'updated')
    list_filter = ('icon', )
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'description', 'icon')

admin.site.register(OurOffer, OurOfferAdmin)
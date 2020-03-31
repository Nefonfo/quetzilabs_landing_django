from django.contrib import admin
from .models import Member, SocialMedia

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ('name', 'position', 'phone', 'email')
    list_filter = ('position',)
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'phone', 'email')

class SocialMediaAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    list_display = ('name', 'link', 'icon')
    list_filter = ('name', 'icon')
    readonly_fields = ('created', 'updated')
    search_fields = ('name', 'link', 'icon')

admin.site.register(Member, MemberAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)